import time
import unittest
from itertools import product

from sudoku.constraints import LittleKillerConstraint
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


def empty_puzzle():
    return SudokuPuzzle([[0] * 9 for _ in range(9)])


class TestLittleKillerConstraint(unittest.TestCase):

    def test_valid_complete_assignment(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 3,
                (1, 1): 8,
                (2, 2): 1,
            })
        )

    def test_invalid_sum(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 3,
                (1, 1): 8,
                (2, 2): 2,
            })
        )

    def test_repeated_digits_allowed(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 4,
                (1, 1): 4,
                (2, 2): 4,
            })
        )

    def test_partial_assignment_valid(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 9})
        )

    def test_partial_assignment_contradiction(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        # 9 + 9 already exceeds 12 - 1.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 9,
                (1, 1): 9,
            })
        )

    def test_single_cell_clue(self):
        constraint = LittleKillerConstraint([(0, 0)], 7)

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 7})
        )

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 6})
        )

    def test_empty_cells_rejected(self):
        with self.assertRaises(ValueError):
            LittleKillerConstraint([], 10)

    def test_infeasible_sum_rejected(self):
        with self.assertRaises(ValueError):
            LittleKillerConstraint([(0, 0), (1, 1)], 1)

        with self.assertRaises(ValueError):
            LittleKillerConstraint([(0, 0), (1, 1)], 19)

    def test_duplicate_cells_rejected(self):
        with self.assertRaises(ValueError):
            LittleKillerConstraint(
                [(0, 0), (1, 1), (0, 0)], 12
            )


class TestLittleKillerPropagation(unittest.TestCase):

    def test_basic_propagation(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1)], 6
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (1, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 0)], {1, 2, 3, 4, 5})
        self.assertEqual(domains[(1, 1)], {1, 2, 3, 4, 5})

    def test_supported_candidate_pruning(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1), (2, 2)], 20
        )

        domains = {
            (0, 0): {1, 9},
            (1, 1): {9},
            (2, 2): {1, 2, 9},
        }

        self.assertTrue(constraint.propagate(domains))

        # 20 = 9 + 9 + 2 or 20 = 1 + 9 + ... no:
        # 1 + 9 + 10 is impossible, so (0,0) = 9.
        self.assertEqual(domains[(0, 0)], {9})
        self.assertEqual(domains[(2, 2)], {2})

    def test_contradiction_raises(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1)], 17
        )

        domains = {
            (0, 0): {1, 2},
            (1, 1): {1, 2},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_does_not_mutate_domains(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1)], 17
        )

        domains = {
            (0, 0): {1, 2},
            (1, 1): {1, 2},
        }

        snapshot = {
            cell: set(values)
            for cell, values in domains.items()
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

        self.assertEqual(domains, snapshot)

    def test_no_change_returns_false(self):
        constraint = LittleKillerConstraint(
            [(0, 0), (1, 1)], 10
        )

        domains = {
            (0, 0): {1, 9},
            (1, 1): {1, 9},
        }

        self.assertFalse(constraint.propagate(domains))

    def test_brute_force_supported_values(self):
        cells = [(0, 0), (1, 1), (2, 2)]
        constraint = LittleKillerConstraint(cells, 15)

        domains = {
            (0, 0): {1, 4, 7},
            (1, 1): {2, 5, 8},
            (2, 2): {3, 6, 9},
        }

        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            if sum(values) == 15:
                for cell, value in zip(cells, values):
                    supported[cell].add(value)

        self.assertTrue(any(supported.values()))

        constraint.propagate(domains)

        for cell in cells:
            self.assertEqual(
                domains[cell],
                supported[cell],
                f"Propagation mismatch at {cell}"
            )

    def test_long_diagonal_propagation_is_fast(self):
        cells = [(i, i) for i in range(9)]
        constraint = LittleKillerConstraint(cells, 45)

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


class TestLittleKillerIntegration(unittest.TestCase):

    def test_registration(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_little_killer(
            [(0, 0), (1, 1), (2, 2)], 12
        )

        self.assertEqual(
            len(puzzle.constraints), baseline + 1
        )

    def test_diagonal_helper_down_right(self):
        cells = SudokuPuzzle.little_killer_cells(
            (-1, -1), "down-right"
        )

        self.assertEqual(
            cells,
            [(i, i) for i in range(9)]
        )

    def test_diagonal_helper_up_left(self):
        cells = SudokuPuzzle.little_killer_cells(
            (5, 9), "up-left"
        )

        self.assertEqual(
            cells,
            [(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)]
        )

    def test_diagonal_helper_invalid_direction(self):
        with self.assertRaises(ValueError):
            SudokuPuzzle.little_killer_cells(
                (-1, -1), "sideways"
            )

    def test_diagonal_helper_outside_grid(self):
        with self.assertRaises(ValueError):
            SudokuPuzzle.little_killer_cells(
                (9, 9), "down-right"
            )

    def test_orthogonal_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_little_killer(
                [(0, 0), (0, 1)], 10
            )

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_little_killer(
                [(8, 8), (9, 9)], 10
            )

    def test_infeasible_sum_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_little_killer(
                [(0, 0), (1, 1)], 100
            )

    def test_solver_integration(self):
        puzzle = empty_puzzle()

        cells = SudokuPuzzle.little_killer_cells(
            (-1, 6), "down-right"
        )

        puzzle.add_little_killer(cells, 12)

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        self.assertEqual(
            sum(solution[cell] for cell in cells), 12
        )

        self.assertEqual(
            validate_solution(puzzle, solution), []
        )

    def test_mixed_variants(self):
        puzzle = empty_puzzle()

        puzzle.add_little_killer(
            [(0, 2), (1, 1), (2, 0)], 10
        )
        puzzle.add_inequality((8, 0), (8, 1), "<")
        puzzle.add_even_cell((4, 4))

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(
            validate_solution(puzzle, solution), []
        )


class TestLittleKillerValidation(unittest.TestCase):

    def test_validator_accepts_valid_clue(self):
        puzzle = empty_puzzle()

        # R9C1 + R8C2 + R7C3 = 3 + 8 + 1 = 12.
        puzzle.add_little_killer(
            [(8, 0), (7, 1), (6, 2)], 12
        )

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_violation(self):
        puzzle = empty_puzzle()

        # The same diagonal sums to 12, not 13.
        puzzle.add_little_killer(
            [(8, 0), (7, 1), (6, 2)], 13
        )

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Little Killer violation" in error
                and "expected 13" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete(self):
        puzzle = empty_puzzle()
        puzzle.add_little_killer(
            [(8, 0), (7, 1), (6, 2)], 12
        )

        solution = solved_assignment()
        del solution[(7, 1)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Little Killer is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
