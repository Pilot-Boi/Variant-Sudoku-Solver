import csv
import tempfile
import unittest
from pathlib import Path

from benchmarks.ctc_metadata import (
    CTC_METADATA,
    duration_to_seconds,
    get_ctc_metadata,
    seconds_to_duration,
)
from benchmarks.run_benchmarks import (
    BENCHMARK_FIELDNAMES,
    CTC_COMPARISON_FIELDNAMES,
    compute_video_ratio,
    ctc_fields,
    discover_puzzles,
    write_benchmark_csv,
    write_ctc_comparison,
)


CTC_FIELD_KEYS = [
    "ctc_catalogue_id",
    "ctc_title",
    "ctc_setter",
    "ctc_human_solver",
    "ctc_video_date",
    "ctc_video_duration",
    "ctc_video_seconds",
    "video_to_solver_ratio",
]


def fake_result(name="Fake Puzzle", elapsed=0.5):
    """A complete benchmark result row without solving."""
    return {
        "puzzle": name,
        "status": "unique",
        "solutions": 1,
        "validation": "PASS",
        "givens": 20,
        "constraints": 30,
        "elapsed_seconds": elapsed,
        "min_seconds": elapsed,
        "max_seconds": elapsed,
        "trials": 5,
        "search_decisions": 10,
        "solving_method": "Propagation + Search",
        "backtracks": 3,
        "propagation_rounds": 40,
        **ctc_fields(name, elapsed),
    }


class TestCtcMetadata(unittest.TestCase):

    def test_center_focus_lookup(self):
        metadata = get_ctc_metadata("Center Focus — DedaKosta")

        self.assertIsNotNone(metadata)
        self.assertEqual(metadata["catalogue_id"], 9118)
        self.assertEqual(metadata["title"], "Center Focus")
        self.assertEqual(metadata["setter"], "DedaKosta")
        self.assertEqual(metadata["human_solver"], "Mark")
        self.assertEqual(metadata["video_date"], "2026-09-12")
        self.assertEqual(metadata["video_duration"], "02:15:39")
        self.assertEqual(metadata["video_seconds"], 8139)

    def test_metadata_matches_discovered_puzzle(self):
        discovered = discover_puzzles()

        for name in CTC_METADATA:
            self.assertIn(name, discovered)

    def test_unknown_puzzle_returns_none(self):
        self.assertIsNone(get_ctc_metadata("No Such Puzzle"))

    def test_duration_to_seconds(self):
        self.assertEqual(duration_to_seconds("02:15:39"), 8139)
        self.assertEqual(duration_to_seconds("1:00:00"), 3600)
        self.assertEqual(duration_to_seconds("15:39"), 939)
        self.assertEqual(duration_to_seconds("0:05"), 5)

    def test_duration_matches_registered_seconds(self):
        for name, metadata in CTC_METADATA.items():
            with self.subTest(puzzle=name):
                self.assertEqual(
                    duration_to_seconds(
                        metadata["video_duration"]
                    ),
                    metadata["video_seconds"],
                )

    def test_invalid_duration_rejected(self):
        with self.assertRaises(ValueError):
            duration_to_seconds("8139")

        with self.assertRaises(ValueError):
            duration_to_seconds("1:2:3:4")

    def test_seconds_to_duration(self):
        self.assertEqual(seconds_to_duration(8139), "2:15:39")
        self.assertEqual(seconds_to_duration(939), "15:39")
        self.assertEqual(seconds_to_duration(5), "0:05")


class TestCtcFields(unittest.TestCase):

    def test_ratio_calculation(self):
        self.assertEqual(
            compute_video_ratio(8139, 0.5),
            16278.0
        )

        self.assertEqual(
            compute_video_ratio(8139, 0.14),
            round(8139 / 0.14, 1)
        )

    def test_zero_runtime_is_safe(self):
        self.assertIsNone(compute_video_ratio(8139, 0))
        self.assertIsNone(compute_video_ratio(8139, 0.0))
        self.assertIsNone(compute_video_ratio(8139, 1e-12))
        self.assertIsNone(compute_video_ratio(None, 0.5))

    def test_ctc_puzzle_fields(self):
        fields = ctc_fields("Center Focus — DedaKosta", 0.5)

        self.assertEqual(fields["ctc_catalogue_id"], 9118)
        self.assertEqual(fields["ctc_title"], "Center Focus")
        self.assertEqual(fields["ctc_setter"], "DedaKosta")
        self.assertEqual(fields["ctc_human_solver"], "Mark")
        self.assertEqual(fields["ctc_video_date"], "2026-09-12")
        self.assertEqual(
            fields["ctc_video_duration"], "02:15:39"
        )
        self.assertEqual(fields["ctc_video_seconds"], 8139)
        self.assertEqual(
            fields["video_to_solver_ratio"], 16278.0
        )

    def test_non_ctc_puzzle_fields_blank(self):
        fields = ctc_fields("Thermo Sudoku #001", 0.5)

        for key in CTC_FIELD_KEYS:
            self.assertEqual(fields[key], "", key)

    def test_incomplete_metadata_handled(self):
        CTC_METADATA["__test_incomplete__"] = {
            "catalogue_id": 1,
            "title": "Partial",
        }

        try:
            fields = ctc_fields("__test_incomplete__", 0.5)

            self.assertEqual(fields["ctc_catalogue_id"], 1)
            self.assertEqual(fields["ctc_title"], "Partial")
            self.assertEqual(fields["ctc_setter"], "")
            self.assertEqual(fields["ctc_human_solver"], "")
            self.assertEqual(fields["ctc_video_seconds"], "")

            # Without video seconds, no ratio is produced.
            self.assertEqual(
                fields["video_to_solver_ratio"], ""
            )

        finally:
            del CTC_METADATA["__test_incomplete__"]

    def test_ratio_blank_for_unusable_runtime(self):
        fields = ctc_fields("Center Focus — DedaKosta", 0)

        self.assertEqual(fields["video_to_solver_ratio"], "")
        self.assertEqual(fields["ctc_catalogue_id"], 9118)


class TestBenchmarkCsvOutput(unittest.TestCase):

    def test_existing_fields_preserved(self):
        for field in [
            "puzzle",
            "status",
            "solutions",
            "validation",
            "givens",
            "constraints",
            "elapsed_seconds",
            "min_seconds",
            "max_seconds",
            "trials",
            "search_decisions",
            "solving_method",
            "backtracks",
            "propagation_rounds",
        ]:
            self.assertIn(field, BENCHMARK_FIELDNAMES)

    def test_new_fields_present(self):
        for field in CTC_FIELD_KEYS:
            self.assertIn(field, BENCHMARK_FIELDNAMES)

    def test_benchmark_csv_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"

            write_benchmark_csv(
                [fake_result("Center Focus — DedaKosta")],
                path,
            )

            with path.open(encoding="utf-8") as file:
                reader = csv.DictReader(file)

                self.assertEqual(
                    reader.fieldnames,
                    BENCHMARK_FIELDNAMES,
                )

                rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(
                rows[0]["ctc_catalogue_id"], "9118"
            )

    def test_non_ctc_rows_have_blank_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"

            write_benchmark_csv(
                [fake_result("Ordinary Puzzle")],
                path,
            )

            with path.open(encoding="utf-8") as file:
                rows = list(csv.DictReader(file))

            for key in CTC_FIELD_KEYS:
                self.assertEqual(rows[0][key], "", key)


class TestCtcComparisonCsv(unittest.TestCase):

    def test_comparison_contains_only_ctc_puzzles(self):
        results = [
            fake_result("Ordinary Puzzle"),
            fake_result("Center Focus — DedaKosta", 0.5),
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "comparison.csv"

            # Operates purely on existing results:
            # no puzzle objects, no solver involved.
            write_ctc_comparison(results, path)

            with path.open(encoding="utf-8") as file:
                reader = csv.DictReader(file)

                self.assertEqual(
                    reader.fieldnames,
                    CTC_COMPARISON_FIELDNAMES,
                )

                rows = list(reader)

        self.assertEqual(len(rows), 1)

        row = rows[0]

        self.assertEqual(row["Catalogue ID"], "9118")
        self.assertEqual(row["Puzzle Title"], "Center Focus")
        self.assertEqual(row["Setter"], "DedaKosta")
        self.assertEqual(row["Human Solver"], "Mark")
        self.assertEqual(row["Video Date"], "2026-09-12")
        self.assertEqual(row["Video Duration"], "02:15:39")
        self.assertEqual(row["Video Seconds"], "8139")
        self.assertEqual(row["Solver Seconds"], "0.5")
        self.assertEqual(row["Video/Solver Ratio"], "16278.0")
        self.assertEqual(row["Search Decisions"], "10")
        self.assertEqual(row["Backtracks"], "3")
        self.assertEqual(row["Propagation Rounds"], "40")
        self.assertEqual(row["Givens"], "20")
        self.assertEqual(row["Constraints"], "30")
        self.assertEqual(row["Solution Status"], "unique")
        self.assertEqual(row["Validation"], "PASS")

    def test_header_only_without_ctc_puzzles(self):
        results = [fake_result("Ordinary Puzzle")]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "comparison.csv"

            write_ctc_comparison(results, path)

            content = path.read_text(encoding="utf-8")
            lines = [
                line for line in content.splitlines() if line
            ]

        self.assertEqual(len(lines), 1)
        self.assertTrue(lines[0].startswith("Catalogue ID,"))


if __name__ == "__main__":
    unittest.main()
