import csv
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.ctc_catalogue_filter import (
    classify_records,
    load_config,
    main,
    normalize_tag,
    parse_catalogue,
    rank_missing_constraints,
    run,
    sort_by_duration,
)


HEADER = [
    "Count", "Video Title", "Link YT", "Length",
    "Time (s)", "Host/Solver", "Supercat",
    "Puzzle Sub-Type / Constraints",
    "Constraint 1", "2", "3",
    "Puzzle Title", "Setter",
]


def fixture_row(
    video="Video",
    link="https://youtube.com/watch?v=x",
    length="1:00:00",
    seconds="3600",
    host="Simon",
    supercat="Sudoku",
    tags=(),
    puzzle="Puzzle",
    setter="Setter",
):
    tags = list(tags)
    constraints = (tags + ["", "", ""])[:3]

    return [
        "1", video, link, length, seconds, host,
        supercat, "; ".join(tags),
        *constraints,
        puzzle, setter,
    ]


def write_fixture(directory, rows):
    path = Path(directory) / "catalogue.csv"

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # The real catalogue starts with a blank row.
        writer.writerow([""] * len(HEADER))
        writer.writerow(HEADER)
        writer.writerows(rows)

    return path


class TestConfigAndNormalization(unittest.TestCase):

    def setUp(self):
        self.config = load_config()

    def test_default_config_loads(self):
        self.assertIn("thermometer", self.config["supported"])
        self.assertIn("little killer", self.config["supported"])

    def test_alias_normalization(self):
        self.assertEqual(
            normalize_tag("Thermo", self.config),
            "Thermometer",
        )
        self.assertEqual(
            normalize_tag("O/E", self.config),
            "Odd/Even",
        )

    def test_unknown_tag_is_preserved(self):
        self.assertEqual(
            normalize_tag("Fog", self.config), "Fog"
        )
        self.assertEqual(
            normalize_tag("  Yin-Yang ", self.config),
            "Yin-Yang",
        )

    def test_blank_tag_is_none(self):
        self.assertIsNone(normalize_tag("   ", self.config))

    def test_custom_config_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"

            path.write_text(
                '{"supported": ["Foo"],'
                ' "aliases": {"Bar": "Foo"},'
                ' "manual_review": []}',
                encoding="utf-8",
            )

            config = load_config(path)

            self.assertEqual(
                normalize_tag("Bar", config), "Foo"
            )
            self.assertIn("foo", config["supported"])


class TestParsing(unittest.TestCase):

    def setUp(self):
        self.config = load_config()

    def test_blank_first_row_and_supercat_filter(self):
        rows = [
            fixture_row(video="A", tags=["Thermo"]),
            fixture_row(video="B", supercat="Crossword"),
            fixture_row(video="C", tags=["Killer"]),
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)
            records, stats = parse_catalogue(path, self.config)

        self.assertEqual(
            [r["video_title"] for r in records],
            ["A", "C"],
        )

        self.assertEqual(stats["total_entries"], 3)
        self.assertEqual(stats["sudoku_entries"], 2)
        self.assertEqual(stats["excluded_entries"], 1)

    def test_fields_extracted(self):
        rows = [
            fixture_row(
                video="V", link="L", length="2:00:00",
                seconds="7200", host="Mark",
                tags=["Thermo", "Renban"],
                puzzle="P", setter="S",
            ),
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)
            record = parse_catalogue(path, self.config)[0][0]

        self.assertEqual(record["video_title"], "V")
        self.assertEqual(record["puzzle_title"], "P")
        self.assertEqual(record["setter"], "S")
        self.assertEqual(record["host"], "Mark")
        self.assertEqual(record["link"], "L")
        self.assertEqual(record["length"], "2:00:00")
        self.assertEqual(record["seconds"], 7200)
        self.assertEqual(
            record["tags"], ["Thermometer", "Renban"]
        )

    def test_missing_header_raises(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"

            path.write_text("a,b,c\n1,2,3\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                parse_catalogue(path, self.config)

    def test_tags_from_combined_field_not_discarded(self):
        # A tag present only in the semicolon field must
        # still be collected.
        row = fixture_row(tags=["Thermo"])
        combined_index = HEADER.index(
            "Puzzle Sub-Type / Constraints"
        )
        row[combined_index] = "Thermo; Mystery Rule"

        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, [row])
            record = parse_catalogue(path, self.config)[0][0]

        self.assertIn("Mystery Rule", record["tags"])


class TestClassification(unittest.TestCase):

    def setUp(self):
        self.config = load_config()

    def classify(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)
            records, stats = parse_catalogue(path, self.config)

        return classify_records(records, self.config)

    def test_all_supported_is_compatible(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(tags=["Thermo", "Killer", "XV"]),
        ])

        self.assertEqual(len(compatible), 1)
        self.assertEqual(nearly, [])
        self.assertEqual(unsupported, [])

    def test_one_or_two_missing_is_nearly(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(video="one", tags=["Thermo", "Fog"]),
            fixture_row(
                video="two",
                tags=["Killer", "Fog", "Yin-Yang"],
            ),
        ])

        self.assertEqual(compatible, [])
        self.assertEqual(len(nearly), 2)
        self.assertEqual(unsupported, [])

        self.assertEqual(nearly[0]["missing"], ["Fog"])
        self.assertEqual(
            nearly[1]["missing"], ["Fog", "Yin-Yang"]
        )

    def test_three_missing_is_unsupported(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(
                tags=["Fog", "Yin-Yang", "Loop"]
            ),
        ])

        self.assertEqual(compatible, [])
        self.assertEqual(nearly, [])
        self.assertEqual(len(unsupported), 1)

    def test_unknown_tags_never_discarded(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(tags=["Thermo", "Totally New Rule"]),
        ])

        self.assertEqual(
            nearly[0]["missing"], ["Totally New Rule"]
        )

    def test_manual_review_flags(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(tags=["Classic", "6x6"]),
        ])

        self.assertEqual(nearly[0]["flags"], ["6x6"])
        self.assertEqual(nearly[0]["missing"], ["6x6"])

    def test_untagged_puzzle_flagged_for_review(self):
        compatible, nearly, unsupported = self.classify([
            fixture_row(tags=[]),
        ])

        self.assertEqual(len(compatible), 1)
        self.assertEqual(
            compatible[0]["flags"],
            ["No constraint tags listed"],
        )


class TestRankingAndSorting(unittest.TestCase):

    def setUp(self):
        self.config = load_config()

    def test_missing_constraint_ranking(self):
        rows = [
            fixture_row(video="a", tags=["Thermo", "Fog"]),
            fixture_row(video="b", tags=["Killer", "Fog"]),
            fixture_row(
                video="c", tags=["Fog", "Yin-Yang"]
            ),
            fixture_row(
                video="d",
                tags=["Loop", "Yin-Yang", "Sandwich"],
            ),
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)
            records, stats = parse_catalogue(path, self.config)

        compatible, nearly, unsupported = classify_records(
            records, self.config
        )

        ranking = rank_missing_constraints(nearly, unsupported)

        by_name = {
            entry["constraint"]: entry for entry in ranking
        }

        # Fog alone blocks puzzles a and b.
        self.assertEqual(by_name["Fog"]["unlocks_alone"], 2)
        self.assertEqual(
            by_name["Fog"]["nearly_appearances"], 3
        )
        self.assertEqual(
            by_name["Fog"]["total_appearances"], 3
        )

        self.assertEqual(
            by_name["Yin-Yang"]["unlocks_alone"], 0
        )
        self.assertEqual(
            by_name["Yin-Yang"]["total_appearances"], 2
        )

        # Fog ranks first.
        self.assertEqual(ranking[0]["constraint"], "Fog")

    def test_sort_by_duration_descending(self):
        records = [
            {"seconds": 100},
            {"seconds": 900},
            {"seconds": 500},
        ]

        ordered = sort_by_duration(records)

        self.assertEqual(
            [r["seconds"] for r in ordered],
            [900, 500, 100],
        )


class TestRunAndOutputs(unittest.TestCase):

    def run_fixture(self, rows, **kwargs):
        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)

            output_dir = Path(directory) / "out"

            results = run(
                catalogue=path,
                output_dir=output_dir,
                **kwargs,
            )

            files = {
                name: list(
                    csv.DictReader(
                        file_path.open(encoding="utf-8")
                    )
                )
                for name, file_path in results["paths"].items()
            }

        return results, files

    def test_output_files_and_columns(self):
        rows = [
            fixture_row(
                video="ok", seconds="100",
                tags=["Thermo"],
            ),
            fixture_row(
                video="near", seconds="200",
                tags=["Killer", "Fog"],
            ),
        ]

        results, files = self.run_fixture(rows)

        compatible = files["compatible"]
        nearly = files["nearly"]
        missing = files["missing"]

        self.assertEqual(len(compatible), 1)
        self.assertEqual(
            compatible[0]["Video Title"], "ok"
        )
        self.assertEqual(
            compatible[0]["Constraints"], "Thermometer"
        )

        self.assertEqual(len(nearly), 1)
        self.assertEqual(
            nearly[0]["Missing Constraints"], "Fog"
        )

        self.assertEqual(missing[0]["Constraint"], "Fog")
        self.assertEqual(missing[0]["Unlocks Alone"], "1")

        for row in compatible + nearly:
            for column in (
                "Video Title", "Puzzle Title", "Setter",
                "Host/Solver", "Link YT", "Length",
                "Time (s)", "Constraints", "Review Flags",
            ):
                self.assertIn(column, row)

    def test_header_only_when_no_matches(self):
        rows = [
            fixture_row(supercat="Crossword"),
        ]

        results, files = self.run_fixture(rows)

        self.assertEqual(files["compatible"], [])
        self.assertEqual(files["nearly"], [])
        self.assertEqual(files["missing"], [])

    def test_min_minutes_filter(self):
        rows = [
            fixture_row(
                video="short", seconds="1800",
                tags=["Thermo"],
            ),
            fixture_row(
                video="long", seconds="7200",
                tags=["Thermo"],
            ),
        ]

        results, files = self.run_fixture(
            rows, min_minutes=60
        )

        self.assertEqual(len(files["compatible"]), 1)
        self.assertEqual(
            files["compatible"][0]["Video Title"], "long"
        )

    def test_top_limit(self):
        rows = [
            fixture_row(
                video=f"v{i}", seconds=str(100 * (i + 1)),
                tags=["Thermo"],
            )
            for i in range(5)
        ]

        results, files = self.run_fixture(rows, top=2)

        self.assertEqual(len(files["compatible"]), 2)

        # The two longest videos survive, sorted
        # descending by duration.
        self.assertEqual(
            [r["Video Title"] for r in files["compatible"]],
            ["v4", "v3"],
        )


class TestSummaryStatistics(unittest.TestCase):
    """Full-catalogue statistics versus filtered exports."""

    def fixture_rows(self):
        return [
            # Compatible, varying durations.
            fixture_row(
                video="c-long", seconds="7200",
                tags=["Thermo"],
            ),
            fixture_row(
                video="c-short", seconds="600",
                tags=["Killer"],
            ),
            fixture_row(
                video="c-mid", seconds="4000",
                tags=["XV"],
            ),
            # Nearly compatible (short video, Fog).
            fixture_row(
                video="n-short", seconds="300",
                tags=["Thermo", "Fog"],
            ),
            # Unsupported (short video).
            fixture_row(
                video="u-short", seconds="200",
                tags=["Fog", "Loop", "Yin-Yang"],
            ),
            # Excluded entirely.
            fixture_row(video="x", supercat="Crossword"),
        ]

    def run_fixture(self, **kwargs):
        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(
                directory, self.fixture_rows()
            )

            results = run(
                catalogue=path,
                output_dir=Path(directory) / "out",
                **kwargs,
            )

            files = {
                name: list(
                    csv.DictReader(
                        file_path.open(encoding="utf-8")
                    )
                )
                for name, file_path in results["paths"].items()
            }

        return results, files

    def test_full_counts_unaffected_by_top(self):
        results, files = self.run_fixture(top=1)

        self.assertEqual(len(results["full"]["compatible"]), 3)
        self.assertEqual(len(results["full"]["nearly"]), 1)
        self.assertEqual(
            len(results["full"]["unsupported"]), 1
        )

        # Only the export is capped.
        self.assertEqual(len(files["compatible"]), 1)
        self.assertEqual(
            files["compatible"][0]["Video Title"], "c-long"
        )

    def test_full_counts_unaffected_by_min_minutes(self):
        results, files = self.run_fixture(min_minutes=60)

        self.assertEqual(len(results["full"]["compatible"]), 3)
        self.assertEqual(len(results["full"]["nearly"]), 1)
        self.assertEqual(
            len(results["full"]["unsupported"]), 1
        )

        # The filtered view reflects the duration cut.
        filtered = results["filtered"]

        self.assertEqual(len(filtered["compatible"]), 2)
        self.assertEqual(len(filtered["nearly"]), 0)
        self.assertEqual(len(filtered["unsupported"]), 0)

        self.assertEqual(len(files["compatible"]), 2)
        self.assertEqual(files["nearly"], [])

    def test_no_filter_means_no_filtered_view(self):
        results, files = self.run_fixture()

        self.assertIsNone(results["filtered"])

    def test_categories_sum_to_sudoku_total(self):
        results, files = self.run_fixture(
            min_minutes=60, top=1
        )

        total = sum(
            len(bucket)
            for bucket in results["full"].values()
        )

        self.assertEqual(
            total, results["stats"]["sudoku_entries"]
        )
        self.assertEqual(results["stats"]["sudoku_entries"], 5)
        self.assertEqual(results["stats"]["total_entries"], 6)

    def test_ranking_uses_all_sudoku_puzzles(self):
        # The only Fog puzzles are short videos; the
        # duration filter must not remove them from
        # the ranking.
        results, files = self.run_fixture(
            min_minutes=60, top=1
        )

        by_name = {
            entry["constraint"]: entry
            for entry in results["ranking"]
        }

        self.assertEqual(by_name["Fog"]["unlocks_alone"], 1)
        self.assertEqual(
            by_name["Fog"]["total_appearances"], 2
        )

        self.assertEqual(
            files["missing"][0]["Constraint"], "Fog"
        )

    def test_csv_schemas_unchanged(self):
        results, files = self.run_fixture()

        with_rows = files["compatible"][0]

        self.assertEqual(
            list(with_rows.keys()),
            [
                "Video Title", "Puzzle Title", "Setter",
                "Host/Solver", "Link YT", "Length",
                "Time (s)", "Constraints", "Review Flags",
            ],
        )

        nearly_row = files["nearly"][0]

        self.assertEqual(
            list(nearly_row.keys()),
            [
                "Video Title", "Puzzle Title", "Setter",
                "Host/Solver", "Link YT", "Length",
                "Time (s)", "Constraints",
                "Missing Constraints", "Review Flags",
            ],
        )

        self.assertEqual(
            list(files["missing"][0].keys()),
            [
                "Constraint", "Unlocks Alone",
                "Appears In Nearly Compatible",
                "Total Appearances",
            ],
        )


class TestConsoleOutput(unittest.TestCase):

    def capture(self, extra_args):
        rows = TestSummaryStatistics().fixture_rows()

        with tempfile.TemporaryDirectory() as directory:
            path = write_fixture(directory, rows)

            buffer = io.StringIO()

            with redirect_stdout(buffer):
                main([
                    "--catalogue", str(path),
                    "--output-dir",
                    str(Path(directory) / "out"),
                    *extra_args,
                ])

        return buffer.getvalue()

    def test_sections_and_full_counts(self):
        output = self.capture(
            ["--min-minutes", "60", "--top", "1"]
        )

        self.assertIn("CATALOGUE OVERVIEW", output)
        self.assertIn("COMPATIBILITY — FULL CATALOGUE", output)
        self.assertIn("FILTERED RESULTS", output)
        self.assertIn("CSV EXPORT SUMMARY", output)
        self.assertIn("MISSING CONSTRAINTS (TOP 10)", output)

        def stat_line(label, value):
            for line in output.splitlines():
                if line.startswith(label):
                    return line.endswith(str(value))
            return False

        # Overview reflects the whole input file.
        self.assertTrue(stat_line("Total entries:", 6))
        self.assertTrue(
            stat_line("Sudoku puzzles analyzed:", 5)
        )
        self.assertTrue(
            stat_line("Non-Sudoku entries excluded:", 1)
        )

        # Full-catalogue compatibility is unfiltered.
        self.assertTrue(
            stat_line("Potentially compatible:", 3)
        )

        # Filtered and exported counts differ from the
        # full-catalogue counts.
        self.assertTrue(
            stat_line("Sudoku puzzles in filter:", 2)
        )
        self.assertTrue(
            stat_line("Maximum rows per puzzle CSV:", 1)
        )
        self.assertTrue(
            stat_line("Compatible puzzles exported:", 1)
        )

    def test_filtered_section_omitted_without_filter(self):
        output = self.capture([])

        self.assertNotIn("FILTERED RESULTS", output)
        self.assertIn("unlimited", output)

    def test_ranking_legend_present(self):
        output = self.capture([])

        self.assertIn("Unlocks alone:", output)
        self.assertIn("Total appearances:", output)
        self.assertIn("Fog", output)


if __name__ == "__main__":
    unittest.main()
