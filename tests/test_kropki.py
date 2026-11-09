import unittest
from pathlib import Path

from sudoku.constraints import (
    KropkiConstraint,
    NegativeKropkiConstraint,
    generate_orthogonal_pairs,
)
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution
from visualization.html_renderer import render_puzzle


SOLVED_GRID = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def solved_assignment():
    return {
        (r, c): SOLVED_GRID[r][c]
        for r in range(9)
        for c in range(9)
    }


def empty_puzzle():
    return SudokuPuzzle([[0] * 9 for _ in range(9)])


class TestKropkiConstraint(unittest.TestCase):

    def test_white_dot_valid(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 4, (0, 1): 5})
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 5, (0, 1): 4})
        )

    def test_white_dot_invalid(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 4, (0, 1): 6})
        )

    def test_black_dot_valid(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "black")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 3, (0, 1): 6})
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 8, (0, 1): 4})
        )

    def test_black_dot_invalid(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "black")

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 3, (0, 1): 7})
        )

    def test_one_two_satisfies_both_dot_types(self):
        white = KropkiConstraint((0, 0), (0, 1), "white")
        black = KropkiConstraint((0, 0), (0, 1), "black")

        assignment = {(0, 0): 1, (0, 1): 2}

        self.assertTrue(white.is_satisfied(assignment))
        self.assertTrue(black.is_satisfied(assignment))

        assignment = {(0, 0): 2, (0, 1): 1}

        self.assertTrue(white.is_satisfied(assignment))
        self.assertTrue(black.is_satisfied(assignment))

    def test_partial_assignment(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        self.assertTrue(constraint.is_satisfied({}))
        self.assertTrue(
            constraint.is_satisfied({(0, 0): 9})
        )

    def test_invalid_dot_type_rejected(self):
        with self.assertRaises(ValueError):
            KropkiConstraint((0, 0), (0, 1), "red")

    def test_identical_cells_rejected(self):
        with self.assertRaises(ValueError):
            KropkiConstraint((0, 0), (0, 0), "white")


class TestKropkiPropagation(unittest.TestCase):

    def test_white_bidirectional_propagation(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        domains = {
            (0, 0): {5},
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 1)], {4, 6})

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): {1},
        }

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 0)], {2})

    def test_black_bidirectional_propagation(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "black")

        domains = {
            (0, 0): {3},
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 1)], {6})

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): {8},
        }

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 0)], {4})

    def test_black_dot_prunes_unpairable_digits(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "black")

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        # 5, 7, and 9 have no 1:2 partner among 1-9.
        self.assertEqual(
            domains[(0, 0)],
            {1, 2, 3, 4, 6, 8}
        )
        self.assertEqual(
            domains[(0, 1)],
            {1, 2, 3, 4, 6, 8}
        )

    def test_contradiction_raises(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        domains = {
            (0, 0): {1},
            (0, 1): {3, 5, 7},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_no_change_returns_false(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        domains = {
            (0, 0): {4, 6},
            (0, 1): {5},
        }

        self.assertFalse(constraint.propagate(domains))

    def test_brute_force_white(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "white")

        domains = {
            (0, 0): {1, 3, 5, 9},
            (0, 1): {2, 5, 6},
        }

        supported_a = {
            x for x in domains[(0, 0)]
            if any(abs(x - y) == 1 for y in domains[(0, 1)])
        }
        supported_b = {
            y for y in domains[(0, 1)]
            if any(abs(x - y) == 1 for x in domains[(0, 0)])
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 0)], supported_a)
        self.assertEqual(domains[(0, 1)], supported_b)

    def test_brute_force_black(self):
        constraint = KropkiConstraint((0, 0), (0, 1), "black")

        domains = {
            (0, 0): {1, 2, 4, 7},
            (0, 1): {2, 3, 8},
        }

        def ratio(x, y):
            return x == 2 * y or y == 2 * x

        supported_a = {
            x for x in domains[(0, 0)]
            if any(ratio(x, y) for y in domains[(0, 1)])
        }
        supported_b = {
            y for y in domains[(0, 1)]
            if any(ratio(x, y) for x in domains[(0, 0)])
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 0)], supported_a)
        self.assertEqual(domains[(0, 1)], supported_b)


class TestNegativeKropkiConstraint(unittest.TestCase):

    def test_rejects_consecutive_pair(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 4, (0, 1): 5})
        )

    def test_rejects_ratio_pair(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 3, (0, 1): 6})
        )

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 1})
        )

    def test_accepts_unrelated_pair(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 7})
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 9, (0, 1): 5})
        )

    def test_partial_assignment(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 4})
        )

    def test_propagation(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {1},
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        # 2 is both consecutive with and double of 1.
        # Equal digits are not forbidden by negative
        # Kropki itself; row/column rules handle those.
        self.assertEqual(
            domains[(0, 1)],
            {1, 3, 4, 5, 6, 7, 8, 9}
        )

    def test_contradiction_raises(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {1},
            (0, 1): {2},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_brute_force_negative(self):
        constraint = NegativeKropkiConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {1, 4, 6, 8},
            (0, 1): {2, 3, 8, 9},
        }

        def allowed(x, y):
            return (
                abs(x - y) != 1
                and x != 2 * y
                and y != 2 * x
            )

        supported_a = {
            x for x in domains[(0, 0)]
            if any(allowed(x, y) for y in domains[(0, 1)])
        }
        supported_b = {
            y for y in domains[(0, 1)]
            if any(allowed(x, y) for x in domains[(0, 0)])
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 0)], supported_a)
        self.assertEqual(domains[(0, 1)], supported_b)


class TestKropkiPuzzleIntegration(unittest.TestCase):

    def test_orthogonal_pair_count(self):
        self.assertEqual(
            len(generate_orthogonal_pairs()),
            144
        )

    def test_add_kropki_dot(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_kropki_dot((0, 0), (0, 1), "white")
        puzzle.add_kropki_dot((3, 4), (4, 4), "black")

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2
        )

    def test_invalid_dot_type_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (0, 1), "grey")

    def test_nonadjacent_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (0, 2), "white")

    def test_diagonal_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (1, 1), "white")

    def test_identical_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (0, 0), "white")

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 8), (0, 9), "white")

    def test_duplicate_dot_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((0, 0), (0, 1), "white")

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (0, 1), "white")

    def test_conflicting_dot_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((0, 0), (0, 1), "white")

        # Same unordered pair, opposite order, new type.
        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 1), (0, 0), "black")

    def test_negative_constraints_exclude_dots(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_kropki_dot((0, 0), (0, 1), "white")
        puzzle.add_kropki_dot((5, 5), (6, 5), "black")

        puzzle.add_negative_kropki_constraints()

        negative = [
            c for c in puzzle.constraints
            if isinstance(c, NegativeKropkiConstraint)
        ]

        self.assertEqual(len(negative), 142)

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2 + 142
        )

    def test_negative_constraints_idempotent(self):
        puzzle = empty_puzzle()

        puzzle.add_negative_kropki_constraints()
        count = len(puzzle.constraints)

        puzzle.add_negative_kropki_constraints()

        self.assertEqual(len(puzzle.constraints), count)

    def test_dot_after_negative_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_negative_kropki_constraints()

        with self.assertRaises(ValueError):
            puzzle.add_kropki_dot((0, 0), (0, 1), "white")

    def test_no_accidental_negative_constraints(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((0, 0), (0, 1), "white")

        self.assertFalse(
            any(
                isinstance(c, NegativeKropkiConstraint)
                for c in puzzle.constraints
            )
        )

    def test_solver_interaction(self):
        puzzle = empty_puzzle()

        puzzle.add_kropki_dot((0, 0), (0, 1), "white")
        puzzle.add_kropki_dot((4, 4), (5, 4), "black")

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        a = solution[(0, 0)]
        b = solution[(0, 1)]
        self.assertEqual(abs(a - b), 1)

        a = solution[(4, 4)]
        b = solution[(5, 4)]
        self.assertTrue(a == 2 * b or b == 2 * a)

        errors = validate_solution(puzzle, solution)

        self.assertEqual(errors, [])


class TestKropkiValidation(unittest.TestCase):

    def test_validator_accepts_valid_white_dot(self):
        puzzle = empty_puzzle()

        # R2C3 = 2 and R2C4 = 1 are consecutive.
        puzzle.add_kropki_dot((1, 2), (1, 3), "white")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_accepts_valid_black_dot(self):
        puzzle = empty_puzzle()

        # R2C3 = 2 and R2C4 = 1 are in a 1:2 ratio.
        # The same pair satisfies both dot types.
        puzzle.add_kropki_dot((1, 2), (1, 3), "black")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_white_violation(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 and R1C2 = 3 differ by 2.
        puzzle.add_kropki_dot((0, 0), (0, 1), "white")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "White Kropki violation: R1C1 and R1C2"
                in error
                for error in errors
            )
        )

    def test_validator_detects_black_violation(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 and R1C2 = 3 are not in a 1:2 ratio.
        puzzle.add_kropki_dot((0, 0), (0, 1), "black")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Black Kropki violation: R1C1 and R1C2"
                in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete_dot(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((1, 2), (1, 3), "white")

        solution = solved_assignment()
        del solution[(1, 2)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Kropki dot is incomplete" in error
                for error in errors
            )
        )

    def test_validator_detects_negative_violation(self):
        puzzle = empty_puzzle()
        puzzle.add_negative_kropki_constraints()

        # R1C5 = 7 and R1C6 = 8 are consecutive.
        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Negative Kropki violation: the undotted "
                "pair R1C5 and R1C6" in error
                for error in errors
            )
        )

    def test_validator_accepts_valid_negative_pair(self):
        puzzle = empty_puzzle()
        puzzle.add_negative_kropki_constraints()

        # R2C1 = 6 and R3C1 = 1: not consecutive,
        # not in ratio. No error mentions this pair.
        errors = validate_solution(puzzle, solved_assignment())

        self.assertFalse(
            any(
                "R2C1 and R3C1" in error
                for error in errors
            )
        )


class TestKropkiRendering(unittest.TestCase):

    def test_inspector_entries_and_controls(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((0, 1), (0, 2), "white")
        puzzle.add_kropki_dot((4, 2), (4, 3), "black")

        path = render_puzzle(
            puzzle,
            title="kropki render test",
            output="output/test_kropki_render.html",
        )

        try:
            html = path.read_text(encoding="utf-8")

            self.assertIn('"kind": "kropki-white"', html)
            self.assertIn('"kind": "kropki-black"', html)
            self.assertIn("toggleLayer('kropki'", html)
            self.assertIn("Kropki White", html)
            self.assertIn("Kropki Black", html)

            # Two dots render exactly two dot circles.
            self.assertEqual(
                html.count('class="kropki-layer"'),
                2
            )

        finally:
            path.unlink()

    def test_negative_constraints_render_no_dots(self):
        puzzle = empty_puzzle()
        puzzle.add_kropki_dot((0, 1), (0, 2), "white")
        puzzle.add_negative_kropki_constraints()

        path = render_puzzle(
            puzzle,
            title="negative kropki render test",
            output="output/test_kropki_negative_render.html",
        )

        try:
            html = path.read_text(encoding="utf-8")

            self.assertIn('"kind": "kropki-negative"', html)
            self.assertIn("Kropki Negative", html)

            # Only the single positive dot is drawn.
            self.assertEqual(
                html.count('class="kropki-layer"'),
                1
            )

        finally:
            path.unlink()


if __name__ == "__main__":
    unittest.main()
