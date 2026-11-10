import unittest
import urllib.error
from pathlib import Path
from unittest import mock

from tools import sudokupad_importer as importer
from tools.sudokupad_importer import (
    SudokuPadImportError,
    border_pair,
    build_report,
    chevron_inequality,
    classify_import,
    decode_payload,
    decompress_from_base64,
    extract_puzzle_reference,
    fetch_payload,
    fpuz_cell,
    generate_module,
    import_puzzle,
    normalize_color,
    parse_fpuzzles,
    parse_scl,
    parse_zipped_json,
    write_module,
)


FIXTURE = (
    Path(__file__).parent / "fixtures" / "wanddeko_scl.txt"
)

MUT_FIXTURE = (
    Path(__file__).parent
    / "fixtures"
    / "mut_zur_luecke_scl.txt"
)


def wanddeko_payload():
    return FIXTURE.read_text(encoding="utf-8").strip()


def wanddeko_model():
    fmt, data = decode_payload(wanddeko_payload())
    return parse_scl(
        data, "https://sudokupad.app/2004fp6a0r"
    )


def mut_model():
    payload = MUT_FIXTURE.read_text(
        encoding="utf-8"
    ).strip()

    fmt, data = decode_payload(payload)

    return parse_scl(
        data, "https://sudokupad.app/q9tbRnF4Nh"
    )


def synthetic_scl(**overrides):
    """A minimal valid 9x9 SCL dict."""
    data = {
        "metadata": {
            "t": "Test",
            "author": "Tester",
            "rules": (
                "Digits separated by a white dot are "
                "consecutive."
            ),
        },
        "ce": [[None] * 9 for _ in range(9)],
    }

    data.update(overrides)
    return data


class TestReferenceParsing(unittest.TestCase):

    def test_url_forms(self):
        for url in (
            "https://sudokupad.app/2004fp6a0r",
            "https://sudokupad.app/2004fp6a0r/",
            "sudokupad.app/2004fp6a0r",
            "https://sudokupad.app/sudoku/2004fp6a0r",
            "https://sudokupad.app/2004fp6a0r?setting=1",
        ):
            self.assertEqual(
                extract_puzzle_reference(url),
                ("id", "2004fp6a0r"),
                url,
            )

    def test_short_id(self):
        self.assertEqual(
            extract_puzzle_reference("2004fp6a0r"),
            ("id", "2004fp6a0r"),
        )

    def test_raw_data_passthrough(self):
        payload = wanddeko_payload()

        kind, value = extract_puzzle_reference(payload)

        self.assertEqual(kind, "data")
        self.assertEqual(value, payload)

    def test_short_id_is_not_treated_as_data(self):
        # IDs that merely start with letters resembling a
        # prefix must still be treated as IDs.
        self.assertEqual(
            extract_puzzle_reference("sclabc123"),
            ("id", "sclabc123"),
        )

    def test_invalid_reference_rejected(self):
        with self.assertRaises(SudokuPadImportError):
            extract_puzzle_reference("not a puzzle!!")


class TestDecoding(unittest.TestCase):

    def test_lz_decompression(self):
        text = decompress_from_base64(
            wanddeko_payload()[3:]
        )

        self.assertTrue(text.startswith("{id:'penpad"))
        self.assertIn("Wanddeko", text)

    def test_decode_payload_scl(self):
        fmt, data = decode_payload(wanddeko_payload())

        self.assertEqual(fmt, "scl")
        self.assertEqual(
            data["metadata"]["t"], "Wanddeko"
        )
        self.assertEqual(
            data["metadata"]["author"], "Myxo"
        )

    def test_unsupported_encoding_rejected(self):
        with self.assertRaises(SudokuPadImportError):
            decode_payload("zzz" + "A" * 40)

    def test_zipped_json_dialect(self):
        value = parse_zipped_json(
            "{a:'x',b:[,,3],c:#F,d:{e:1.5},f:true}"
        )

        self.assertEqual(
            value,
            {
                "a": "x",
                "b": [None, None, 3],
                "c": "#F",
                "d": {"e": 1.5},
                "f": True,
            },
        )

    def test_zipped_json_elisions(self):
        value = parse_zipped_json("[,,,,,,,,]")

        self.assertEqual(value, [None] * 9)

    def test_normalize_color(self):
        self.assertEqual(normalize_color("#0"), "#000000")
        self.assertEqual(normalize_color("#F"), "#FFFFFF")
        self.assertEqual(
            normalize_color("#aBc"), "#AABBCC"
        )
        self.assertEqual(
            normalize_color("#FFFFFF00"), "#FFFFFF00"
        )


class TestGeometry(unittest.TestCase):

    def test_border_pair_vertical(self):
        self.assertEqual(
            border_pair((3.0, 1.5)),
            ((2, 1), (3, 1)),
        )

    def test_border_pair_horizontal(self):
        self.assertEqual(
            border_pair((5.5, 6.0)),
            ((5, 5), (5, 6)),
        )

    def test_border_pair_rejects_non_border(self):
        self.assertIsNone(border_pair((3.0, 3.0)))
        self.assertIsNone(border_pair((4.5, 4.5)))
        self.assertIsNone(border_pair((0.0, 4.5)))

    def test_chevron_vertical_pair(self):
        # Real Wanddeko sign: vertex above the border,
        # so the upper cell is smaller.
        lesser, greater = chevron_inequality(
            [(3.14, 0.36), (2.86, 0.5), (3.14, 0.64)]
        )

        self.assertEqual(lesser, (2, 0))
        self.assertEqual(greater, (3, 0))

    def test_chevron_horizontal_pair(self):
        # Vertex right of the border: right cell smaller.
        lesser, greater = chevron_inequality(
            [(0.36, 2.86), (0.5, 3.14), (0.64, 2.86)]
        )

        self.assertEqual(lesser, (0, 3))
        self.assertEqual(greater, (0, 2))

    def test_chevron_rejects_other_shapes(self):
        self.assertIsNone(
            chevron_inequality([(0, 0), (9, 9)])
        )
        self.assertIsNone(
            chevron_inequality(
                [(1.5, 1.5), (2.5, 2.5), (3.5, 3.5)]
            )
        )

    def test_fpuz_cell_conversion(self):
        self.assertEqual(fpuz_cell("R1C1"), (0, 0))
        self.assertEqual(fpuz_cell("R9C5"), (8, 4))

        with self.assertRaises(SudokuPadImportError):
            fpuz_cell("X2Y3")


class TestSclParsing(unittest.TestCase):

    def test_wanddeko_metadata(self):
        model = wanddeko_model()

        self.assertEqual(model["title"], "Wanddeko")
        self.assertEqual(model["author"], "Myxo")
        self.assertEqual(model["size"], (9, 9))
        self.assertEqual(model["givens"], {})
        self.assertEqual(len(model["solution"]), 81)

    def test_wanddeko_constraints(self):
        model = wanddeko_model()

        dots = model["constraints"]["kropki"]
        white = [d for d in dots if d[2] == "white"]
        black = [d for d in dots if d[2] == "black"]

        self.assertEqual(len(white), 15)
        self.assertEqual(len(black), 1)
        self.assertEqual(
            black[0], ((5, 5), (5, 6), "black")
        )

        inequalities = model["constraints"]["inequality"]

        self.assertEqual(len(inequalities), 15)
        self.assertIn(((2, 0), (3, 0)), inequalities)

    def test_wanddeko_is_complete(self):
        model = wanddeko_model()

        self.assertEqual(model["unrecognized"], [])
        self.assertEqual(model["ambiguous"], [])
        self.assertEqual(model["manual"], [])
        self.assertEqual(classify_import(model), "Complete")

    def test_given_digit_extraction(self):
        data = synthetic_scl()
        data["ce"][0][0] = {"v": 5}
        data["ce"][8][8] = {"value": "9"}

        model = parse_scl(data)

        self.assertEqual(
            model["givens"],
            {(0, 0): 5, (8, 8): 9},
        )

    def test_invalid_grid_size_rejected(self):
        data = synthetic_scl(
            ce=[[None] * 6 for _ in range(6)]
        )

        with self.assertRaises(SudokuPadImportError):
            parse_scl(data)

    def test_unknown_overlay_reported(self):
        data = synthetic_scl(
            o=[
                {"ct": [3, 1.5], "w": 0.286, "r": 1,
                 "c2": "#F", "c1": "#0"},
                {"ct": [4.5, 4.5], "w": 2.0},
            ]
        )

        model = parse_scl(data)

        self.assertEqual(
            len(model["constraints"]["kropki"]), 1
        )
        self.assertEqual(len(model["unrecognized"]), 1)
        self.assertEqual(
            classify_import(model), "Needs Review"
        )

    def test_duplicate_clue_reported(self):
        data = synthetic_scl(
            o=[
                {"ct": [3, 1.5], "w": 0.286, "r": 1,
                 "c2": "#F", "c1": "#0"},
                {"ct": [3, 1.5], "w": 0.286, "r": 1,
                 "c2": "#F", "c1": "#0"},
            ]
        )

        model = parse_scl(data)

        self.assertEqual(
            len(model["constraints"]["kropki"]), 1
        )
        self.assertTrue(
            any(
                "Duplicate" in note
                for note in model["ambiguous"]
            )
        )

    def test_dots_without_rules_text_are_ambiguous(self):
        data = synthetic_scl(
            o=[
                {"ct": [3, 1.5], "w": 0.286, "r": 1,
                 "c2": "#F", "c1": "#0"},
            ]
        )
        data["metadata"]["rules"] = "Normal sudoku rules."

        model = parse_scl(data)

        self.assertTrue(model["ambiguous"])
        self.assertEqual(
            classify_import(model), "Needs Review"
        )

    def test_unclassifiable_line_is_ambiguous(self):
        data = synthetic_scl(
            l=[{"wp": [[0.5, 0.5], [0.5, 4.5]]}]
        )

        model = parse_scl(data)

        self.assertTrue(model["ambiguous"])


class TestMutZurLuecke(unittest.TestCase):
    """Regression tests for the second real puzzle."""

    def test_metadata_from_cage_objects(self):
        model = mut_model()

        self.assertEqual(model["title"], "Mut zur Lücke!")
        self.assertEqual(model["author"], "Wuschel")
        self.assertIn(
            "inequality sign", model["rules"].lower()
        )
        self.assertEqual(len(model["solution"]), 81)
        self.assertTrue(
            model["solution"].startswith("467953812")
        )

        # Original strings are preserved for the report.
        self.assertEqual(
            len(model["metadata_strings"]), 4
        )

    def test_killer_cages_imported(self):
        model = mut_model()

        cages = model["constraints"]["killer"]

        self.assertEqual(len(cages), 8)

        sums = sorted(total for _, total in cages)

        self.assertEqual(
            sums, [12, 12, 12, 20, 20, 28, 28, 28]
        )

        self.assertIn(
            (((0, 0), (1, 0), (2, 0), (2, 1)), 12),
            cages,
        )

    def test_single_main_diagonal(self):
        model = mut_model()

        self.assertEqual(
            model["constraints"]["diagonal"], ["main"]
        )

    def test_glyph_inequality_orientation(self):
        model = mut_model()

        # The 'V' glyph points down toward the smaller
        # digit: R2C1 < R1C1 (solution: 1 < 4).
        self.assertEqual(
            model["constraints"]["inequality"],
            [((1, 0), (0, 0))],
        )

    def test_no_invented_kropki(self):
        model = mut_model()

        self.assertNotIn("kropki", model["constraints"])

    def test_import_is_complete(self):
        model = mut_model()

        self.assertEqual(model["unrecognized"], [])
        self.assertEqual(model["ambiguous"], [])
        self.assertEqual(model["manual"], [])
        self.assertEqual(classify_import(model), "Complete")

    def test_generated_module_with_single_diagonal(self):
        model = mut_model()

        source = generate_module(model, "ctc_test")

        namespace = {}
        exec(compile(source, "ctc_test.py", "exec"), namespace)

        self.assertEqual(
            namespace["NAME"], "Mut zur Lücke! — Wuschel"
        )

        puzzle = namespace["create_puzzle"]()

        # 27 standard + 8 cages + 1 diagonal + 1 inequality.
        self.assertEqual(len(puzzle.constraints), 37)


class TestCageParsing(unittest.TestCase):

    def cage_model(self, cages, rules=None):
        data = synthetic_scl(ca=cages)

        if rules is not None:
            data["metadata"]["rules"] = rules

        return parse_scl(data)

    def test_numeric_sum_types(self):
        model = self.cage_model([
            {"ce": [[0, 0], [0, 1]], "v": 10},
            {"ce": [[1, 0], [1, 1]], "v": "11"},
            {"ce": [[2, 0], [2, 1]], "v": 12.0},
        ], rules="Digits in cages sum to the total.")

        sums = sorted(
            total
            for _, total in model["constraints"]["killer"]
        )

        self.assertEqual(sums, [10, 11, 12])
        self.assertEqual(model["unrecognized"], [])

    def test_malformed_sums_rejected(self):
        model = self.cage_model([
            {"ce": [[0, 0], [0, 1]], "v": 12.5},
            {"ce": [[1, 0], [1, 1]], "v": "abc"},
            {"ce": [[2, 0], [2, 1]], "v": None},
            {"ce": [[3, 0], [3, 1]], "v": True},
        ])

        self.assertNotIn("killer", model["constraints"])
        self.assertEqual(len(model["unrecognized"]), 4)

    def test_invalid_coordinates_rejected(self):
        model = self.cage_model([
            {"ce": [[0, 0], [0, 9]], "v": 10},
            {"ce": [[0, 0], "bad"], "v": 10},
        ])

        self.assertNotIn("killer", model["constraints"])
        self.assertEqual(len(model["unrecognized"]), 2)

    def test_cage_metadata_extraction(self):
        data = synthetic_scl(ca=[
            {"v": "title: Synthetic "},
            {"v": "author: Someone"},
            {"v": "solution: " + "123456789" * 9},
        ])

        # No metadata dict: everything comes from cages.
        data["metadata"] = {}

        model = parse_scl(data)

        self.assertEqual(model["title"], "Synthetic")
        self.assertEqual(model["author"], "Someone")
        self.assertEqual(len(model["solution"]), 81)

    def test_metadata_dict_takes_priority(self):
        model = self.cage_model([
            {"v": "title: Synthetic"},
        ])

        # The synthetic fixture's metadata dict already
        # provides the title "Test".
        self.assertEqual(model["title"], "Test")
        self.assertIn(
            "title: Synthetic", model["metadata_strings"]
        )

    def test_invalid_solution_metadata_flagged(self):
        model = self.cage_model([
            {"v": "solution: 12345"},
        ])

        self.assertIsNone(model["solution"])
        self.assertTrue(
            any(
                "Invalid solution" in item
                for item in model["unrecognized"]
            )
        )

    def test_unknown_cage_objects_reported(self):
        model = self.cage_model([
            {"v": "fogbank: something"},
            {"v": 12},
        ])

        self.assertNotIn("killer", model["constraints"])
        self.assertEqual(len(model["unrecognized"]), 2)

    def test_missing_metadata_handled(self):
        model = self.cage_model([
            {"ce": [[0, 0], [0, 1]], "v": 10},
        ], rules="Digits in cages sum to the total.")

        self.assertEqual(model["title"], "Test")
        self.assertIsNone(model["solution"])
        self.assertEqual(
            len(model["constraints"]["killer"]), 1
        )


class TestBorderGlyphs(unittest.TestCase):

    def glyph_model(self, glyph, center, rules):
        data = synthetic_scl(
            o=[{
                "ct": list(center), "w": 0.2, "h": 0.2,
                "c1": "#F", "c2": "#F", "r": "f",
                "te": glyph,
            }]
        )
        data["metadata"]["rules"] = rules

        return parse_scl(data)

    def test_text_box_is_not_a_kropki_dot(self):
        # 'r': 'f' means rounded=False: a text box must
        # never be mistaken for a white dot.
        model = self.glyph_model(
            "V", (1, 0.5), "Normal sudoku rules apply."
        )

        self.assertNotIn("kropki", model["constraints"])

    def test_glyph_without_context_is_ambiguous(self):
        model = self.glyph_model(
            "V", (1, 0.5), "Normal sudoku rules apply."
        )

        self.assertNotIn("inequality", model["constraints"])
        self.assertNotIn("xv", model["constraints"])
        self.assertTrue(model["ambiguous"])
        self.assertEqual(
            classify_import(model), "Needs Review"
        )

    def test_v_glyph_with_xv_rules(self):
        model = self.glyph_model(
            "V", (1, 0.5),
            "Cells joined by V sum to 5; cells joined "
            "by X sum to 10.",
        )

        self.assertEqual(
            model["constraints"]["xv"],
            [((0, 0), (1, 0), "V")],
        )

    def test_v_glyph_with_inequality_rules(self):
        model = self.glyph_model(
            "V", (1, 0.5),
            "The inequality sign points towards the "
            "smaller digit.",
        )

        self.assertEqual(
            model["constraints"]["inequality"],
            [((1, 0), (0, 0))],
        )

    def test_horizontal_glyphs(self):
        model = self.glyph_model(
            "<", (0.5, 3),
            "The inequality sign points towards the "
            "smaller digit.",
        )

        self.assertEqual(
            model["constraints"]["inequality"],
            [((0, 2), (0, 3))],
        )

    def test_mismatched_glyph_is_ambiguous(self):
        # '<' on a vertical pair makes no sense.
        model = self.glyph_model(
            "<", (1, 0.5),
            "The inequality sign points towards the "
            "smaller digit.",
        )

        self.assertNotIn("inequality", model["constraints"])
        self.assertTrue(model["ambiguous"])


class TestFpuzzlesParsing(unittest.TestCase):

    def test_basic_fpuzzles(self):
        data = {
            "title": "F",
            "author": "A",
            "ruleset": (
                "Kropki: white dots mark consecutive "
                "cells. Anti-knight applies."
            ),
            "size": 9,
            "grid": [
                [
                    {"value": 5, "given": True}
                    if (r, c) == (0, 0)
                    else {}
                    for c in range(9)
                ]
                for r in range(9)
            ],
            "difference": [{"cells": ["R1C1", "R1C2"]}],
            "xv": [
                {"cells": ["R2C1", "R2C2"], "value": "V"},
            ],
            "antiknight": True,
        }

        model = parse_fpuzzles(data)

        self.assertEqual(model["givens"], {(0, 0): 5})
        self.assertEqual(
            model["constraints"]["kropki"],
            [((0, 0), (0, 1), "white")],
        )
        self.assertEqual(
            model["constraints"]["xv"],
            [((1, 0), (1, 1), "V")],
        )
        self.assertIn(
            "anti-knight",
            model["constraints"]["global"],
        )

    def test_unknown_fpuzzles_feature_reported(self):
        data = {
            "size": 9,
            "grid": [[{} for _ in range(9)]
                     for _ in range(9)],
            "sandwichsum": [{"cell": "R0C1"}],
        }

        model = parse_fpuzzles(data)

        self.assertTrue(
            any(
                "sandwichsum" in item
                for item in model["unrecognized"]
            )
        )

    def test_invalid_size_rejected(self):
        with self.assertRaises(SudokuPadImportError):
            parse_fpuzzles({"size": 6, "grid": []})


class TestNetwork(unittest.TestCase):

    def test_network_failure_wrapped(self):
        with mock.patch.object(
            importer.urllib.request, "urlopen",
            side_effect=urllib.error.URLError("down"),
        ):
            with self.assertRaises(SudokuPadImportError):
                fetch_payload("2004fp6a0r")

    def test_http_error_wrapped(self):
        error = urllib.error.HTTPError(
            "url", 404, "not found", {}, None
        )

        with mock.patch.object(
            importer.urllib.request, "urlopen",
            side_effect=error,
        ):
            with self.assertRaises(SudokuPadImportError):
                fetch_payload("doesnotexist")

    def test_import_from_raw_data_needs_no_network(self):
        with mock.patch.object(
            importer.urllib.request, "urlopen",
            side_effect=AssertionError("network used"),
        ):
            model = import_puzzle(wanddeko_payload())

        self.assertEqual(model["title"], "Wanddeko")


class TestOutputGeneration(unittest.TestCase):

    def test_generated_module_is_valid_python(self):
        model = wanddeko_model()

        source = generate_module(model, "ctc_test")

        compiled = compile(source, "ctc_test.py", "exec")

        namespace = {}
        exec(compiled, namespace)

        self.assertEqual(
            namespace["NAME"], "Wanddeko — Myxo"
        )

        puzzle = namespace["create_puzzle"]()

        # 27 standard + 16 dots + 15 inequalities.
        self.assertEqual(len(puzzle.constraints), 58)

    def test_write_module_refuses_overwrite(self):
        model = wanddeko_model()

        # thermo_001 already exists in puzzles/.
        with self.assertRaises(SudokuPadImportError):
            write_module(model, "thermo_001")

    def test_report_contents(self):
        model = wanddeko_model()

        report = build_report(model)

        self.assertIn("Wanddeko", report)
        self.assertIn("Myxo", report)
        self.assertIn("kropki: 16", report)
        self.assertIn("inequality: 15", report)
        self.assertIn("Classification: Complete", report)

    def test_classification_levels(self):
        model = wanddeko_model()
        self.assertEqual(classify_import(model), "Complete")

        model["ambiguous"].append("something odd")
        self.assertEqual(
            classify_import(model), "Needs Review"
        )

        model["ambiguous"].clear()
        model["unrecognized"].extend(
            ["a", "b", "c", "d", "e"]
        )
        model["constraints"] = {}
        self.assertEqual(
            classify_import(model), "Unsupported"
        )


if __name__ == "__main__":
    unittest.main()
