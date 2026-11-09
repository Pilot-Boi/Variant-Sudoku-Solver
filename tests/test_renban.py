import time
import unittest
from itertools import product

from sudoku.constraints import RenbanConstraint
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution


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


class TestRenbanConstraint(unittest.TestCase):

    def test_valid_unordered_consecutive(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 6,
                (0, 1): 4,
                (0, 2): 7,
                (0, 3): 5,
            })
        )

    def test_invalid_nonconsecutive_set(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 2,
                (0, 2): 4,
            })
        )

    def test_duplicate_digits_rejected(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 4,
                (0, 1): 4,
            })
        )

    def test_partial_assignment_valid(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 2,
                (0, 2): 5,
            })
        )

    def test_partial_assignment_contradiction(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # No 3-digit consecutive interval contains 1 and 7.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 2): 7,
            })
        )

    def test_empty_assignment_valid(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1)]
        )

        self.assertTrue(constraint.is_satisfied({}))

    def test_minimum_length_accepted(self):
        constraint = RenbanConstraint([(0, 0), (0, 1)])

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 8,
                (0, 1): 9,
            })
        )

    def test_maximum_length_accepted(self):
        cells = [(0, c) for c in range(9)]

        constraint = RenbanConstraint(cells)

        self.assertTrue(
            constraint.is_satisfied({
                cell: value
                for cell, value in zip(cells, range(1, 10))
            })
        )

    def test_single_cell_rejected(self):
        with self.assertRaises(ValueError):
            RenbanConstraint([(0, 0)])

    def test_ten_cells_rejected(self):
        cells = [(0, c) for c in range(9)] + [(1, 8)]

        with self.assertRaises(ValueError):
            RenbanConstraint(cells)

    def test_duplicate_cells_rejected(self):
        with self.assertRaises(ValueError):
            RenbanConstraint([(0, 0), (0, 1), (0, 0)])


class TestRenbanPropagation(unittest.TestCase):

    def test_fixed_value_restricts_neighbors(self):
        constraint = RenbanConstraint([(0, 0), (0, 1)])

        domains = {
            (0, 0): {5},
            (0, 1): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 1)], {4, 6})

    def test_window_restriction(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {1},
            (0, 1): set(range(1, 10)),
            (0, 2): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        # Only the interval 1-3 contains 1.
        self.assertTrue(changed)
        self.assertEqual(domains[(0, 1)], {2, 3})
        self.assertEqual(domains[(0, 2)], {2, 3})

    def test_supported_candidate_pruning(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # 9 in the last cell fits the interval 7-9 on
        # its own, but no complete assignment uses it.
        domains = {
            (0, 0): {1, 2},
            (0, 1): {1, 2},
            (0, 2): {1, 2, 3, 9},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 0)], {1, 2})
        self.assertEqual(domains[(0, 1)], {1, 2})
        self.assertEqual(domains[(0, 2)], {3})

    def test_candidates_fit_interval_but_no_assignment(self):
        constraint = RenbanConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # Every candidate fits the interval 1-3, but three
        # distinct digits cannot be drawn from {1, 2}.
        domains = {
            (0, 0): {1, 2},
            (0, 1): {1, 2},
            (0, 2): {1, 2},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_does_not_mutate_domains(self):
        constraint = RenbanConstraint([(0, 0), (0, 1)])

        domains = {
            (0, 0): {4},
            (0, 1): {4},
        }

        snapshot = {
            cell: set(values)
            for cell, values in domains.items()
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

        self.assertEqual(domains, snapshot)

    def test_no_change_returns_false(self):
        constraint = RenbanConstraint([(0, 0), (0, 1)])

        domains = {
            (0, 0): {1, 2},
            (0, 1): {1, 2},
        }

        self.assertFalse(
            constraint.propagate(domains)
        )

    def test_propagation_preserves_supported_values(self):
        cells = [(0, 0), (0, 1), (0, 2), (0, 3)]
        constraint = RenbanConstraint(cells)

        domains = {
            (0, 0): {1, 3, 5},
            (0, 1): {2, 4, 6},
            (0, 2): {3, 5, 7},
            (0, 3): {4, 6, 8},
        }

        # Brute force every complete assignment that
        # satisfies the Renban definition directly.
        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            if len(set(values)) != len(cells):
                continue

            if max(values) - min(values) != len(cells) - 1:
                continue

            for cell, value in zip(cells, values):
                supported[cell].add(value)

        self.assertTrue(
            any(supported.values()),
            "Test setup must admit at least one assignment"
        )

        constraint.propagate(domains)

        for cell in cells:
            self.assertTrue(
                supported[cell] <= domains[cell],
                f"Supported values removed from {cell}"
            )

            self.assertEqual(
                domains[cell],
                supported[cell],
                f"Unsupported values retained in {cell}"
            )

    def test_long_line_propagation_is_fast(self):
        cells = [(0, c) for c in range(9)]
        constraint = RenbanConstraint(cells)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        start = time.perf_counter()
        constraint.propagate(domains)
        elapsed = time.perf_counter() - start

        self.assertLess(
            elapsed, 1.0,
            f"Propagation took {elapsed:.3f}s"
        )

        # A full-length line keeps every digit possible.
        for cell in cells:
            self.assertEqual(domains[cell], set(range(1, 10)))


class TestRenbanIntegration(unittest.TestCase):

    def test_constraint_registration(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_renban([(0, 0), (0, 1), (1, 2)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 1
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            RenbanConstraint
        )

    def test_overlapping_lines_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
        puzzle.add_renban([(1, 0), (0, 1), (1, 2)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2
        )

    def test_diagonal_connections_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_renban([(0, 0), (1, 1), (2, 2)])

        self.assertIsInstance(
            puzzle.constraints[-1],
            RenbanConstraint
        )

    def test_non_adjacent_cells_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_renban([(0, 0), (0, 2)])

    def test_repeated_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_renban([(0, 0), (0, 1), (0, 0)])

    def test_out_of_bounds_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_renban([(8, 8), (8, 9)])

    def test_too_long_line_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        cells = [(0, c) for c in range(9)] + [(1, 8)]

        with self.assertRaises(ValueError):
            puzzle.add_renban(cells)

    def test_single_cell_line_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_renban([(0, 0)])


class TestRenbanValidation(unittest.TestCase):

    def test_validator_accepts_valid_line(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C1..R1C3 = 5, 3, 4: consecutive digits 3-5.
        puzzle.add_renban([(0, 0), (0, 1), (0, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_accepts_overlapping_lines(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # Both lines share R1C2 and R1C3.
        puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
        puzzle.add_renban([(0, 1), (0, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_nonconsecutive_digits(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C4..R1C6 = 6, 7, 8 is fine, but
        # R1C3..R1C4 = 4, 6 is not consecutive.
        puzzle.add_renban([(0, 2), (0, 3)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Renban line digits are not consecutive"
                in error
                for error in errors
            )
        )

    def test_validator_detects_duplicate_digits(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_renban([(0, 0), (0, 1)])

        solution = solved_assignment()
        solution[(0, 1)] = solution[(0, 0)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Renban line repeats a digit" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete_line(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_renban([(0, 0), (0, 1)])

        solution = solved_assignment()
        del solution[(0, 1)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Renban line is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
