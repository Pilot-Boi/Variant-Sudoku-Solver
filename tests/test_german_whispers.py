import unittest

from sudoku.constraints import GermanWhispersConstraint
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution


class TestGermanWhispersConstraint(unittest.TestCase):

    def test_valid_assignment(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 6,
                (0, 2): 1,
            })
        )

    def test_invalid_assignment(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 6,
                (0, 2): 2,
            })
        )

    def test_exact_difference_allowed(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 4,
                (0, 1): 9,
            })
        )

    def test_partial_assignment_valid(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 1): 9})
        )

    def test_partial_assignment_invalid(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 1): 9,
                (0, 2): 6,
            })
        )

    def test_non_adjacent_cells_unconstrained(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # Only the endpoints are assigned; they are not
        # adjacent on the line, so any pair is allowed.
        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 2): 2,
            })
        )

    def test_requires_two_cells(self):
        with self.assertRaises(ValueError):
            GermanWhispersConstraint([(0, 0)])

    def test_duplicate_cells_rejected(self):
        with self.assertRaises(ValueError):
            GermanWhispersConstraint(
                [(0, 0), (0, 1), (0, 0)]
            )


class TestGermanWhispersPropagation(unittest.TestCase):

    def test_five_is_eliminated(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertNotIn(5, domains[(0, 0)])
        self.assertNotIn(5, domains[(0, 1)])

    def test_fixed_value_restricts_neighbor(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        domains = {
            (0, 0): {1},
            (0, 1): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 1)], {6, 7, 8, 9})

    def test_propagation_repeats_until_stable(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {1},
            (0, 1): set(range(1, 10)),
            (0, 2): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 1)], {6, 7, 8, 9})
        self.assertEqual(domains[(0, 2)], {1, 2, 3, 4})

    def test_no_change(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        domains = {
            (0, 0): {1, 2},
            (0, 1): {8, 9},
        }

        self.assertFalse(
            constraint.propagate(domains)
        )

    def test_contradiction_from_five(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        domains = {
            (0, 0): {5},
            (0, 1): set(range(1, 10)),
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_from_close_values(self):
        constraint = GermanWhispersConstraint(
            [(0, 0), (0, 1)]
        )

        domains = {
            (0, 0): {4, 6},
            (0, 1): {4, 6},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)


class TestGermanWhispersIntegration(unittest.TestCase):

    def test_constraint_registration(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_german_whispers(
            [(0, 0), (0, 1), (1, 2)]
        )

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 1
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            GermanWhispersConstraint
        )

    def test_diagonal_connections_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_german_whispers(
            [(0, 0), (1, 1), (2, 2)]
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            GermanWhispersConstraint
        )

    def test_non_adjacent_cells_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_german_whispers(
                [(0, 0), (0, 2)]
            )

    def test_repeated_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_german_whispers(
                [(0, 0), (0, 1), (0, 0)]
            )

    def test_single_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_german_whispers([(0, 0)])

    def test_out_of_grid_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_german_whispers(
                [(8, 8), (8, 9)]
            )

    def test_validator_detects_violation(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_german_whispers([(0, 0), (0, 1)])

        solution = {
            (0, 0): 4,
            (0, 1): 6,
        }

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "German Whispers violation" in error
                for error in errors
            )
        )

    def test_validator_accepts_valid_line(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C7 = 9 and R1C8 = 1 differ by 8.
        puzzle.add_german_whispers([(0, 6), (0, 7)])

        grid = [
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

        solution = {
            (r, c): grid[r][c]
            for r in range(9)
            for c in range(9)
        }

        errors = validate_solution(puzzle, solution)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
