import time
import unittest
from itertools import product

from sudoku.constraints import ArrowConstraint
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


class TestArrowConstraint(unittest.TestCase):

    def test_valid_single_cell_circle(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 9,
                (0, 1): 4,
                (0, 2): 5,
            })
        )

    def test_invalid_arrow_sum(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 9,
                (0, 1): 4,
                (0, 2): 4,
            })
        )

    def test_valid_multi_cell_circle_number(self):
        constraint = ArrowConstraint(
            [(0, 0), (0, 1)],
            [(1, 0), (1, 1), (1, 2)],
        )

        # Circle reads 12; 3 + 4 + 5 = 12.
        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 2,
                (1, 0): 3,
                (1, 1): 4,
                (1, 2): 5,
            })
        )

    def test_multi_cell_circle_order_matters(self):
        constraint = ArrowConstraint(
            [(0, 0), (0, 1)],
            [(1, 0), (1, 1), (1, 2)],
        )

        # Circle reads 21, not 12.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 2,
                (0, 1): 1,
                (1, 0): 3,
                (1, 1): 4,
                (1, 2): 5,
            })
        )

    def test_valid_partial_assignment(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 9,
                (0, 1): 1,
            })
        )

    def test_partial_contradiction_sum_too_high(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        # The shaft already needs at least 9 + 1 = 10.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 3,
                (0, 1): 9,
            })
        )

    def test_partial_contradiction_circle_too_small(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2), (0, 3), (0, 4)],
        )

        # Four shaft digits of 9 exceed any single digit.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 1): 9,
                (0, 2): 9,
                (0, 3): 9,
                (0, 4): 9,
            })
        )

    def test_repeated_arrow_digits_allowed(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(1, 1), (2, 2)],
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 4,
                (1, 1): 2,
                (2, 2): 2,
            })
        )

    def test_empty_circle_rejected(self):
        with self.assertRaises(ValueError):
            ArrowConstraint([], [(0, 0)])

    def test_empty_shaft_rejected(self):
        with self.assertRaises(ValueError):
            ArrowConstraint([(0, 0)], [])

    def test_repeated_cells_rejected(self):
        with self.assertRaises(ValueError):
            ArrowConstraint([(0, 0)], [(0, 1), (0, 0)])

        with self.assertRaises(ValueError):
            ArrowConstraint([(0, 0)], [(0, 1), (0, 1)])


class TestArrowPropagation(unittest.TestCase):

    def test_basic_propagation(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
            (0, 2): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        # Two shaft digits sum to at least 2.
        self.assertEqual(domains[(0, 0)], set(range(2, 10)))

        # Each shaft digit leaves room for the other.
        self.assertEqual(domains[(0, 1)], set(range(1, 9)))
        self.assertEqual(domains[(0, 2)], set(range(1, 9)))

    def test_supported_candidate_pruning(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        # 9 fits each domain but participates in no
        # assignment summing to 5.
        domains = {
            (0, 0): {5},
            (0, 1): {1, 2, 3, 4, 9},
            (0, 2): {1, 2, 3, 4, 9},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 1)], {1, 2, 3, 4})
        self.assertEqual(domains[(0, 2)], {1, 2, 3, 4})

    def test_no_all_different_restriction(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(1, 1), (2, 2)],
        )

        # The only assignment is 2 + 2 = 4: repeated
        # shaft digits must survive propagation.
        domains = {
            (0, 0): {4},
            (1, 1): {2},
            (2, 2): {2},
        }

        self.assertFalse(constraint.propagate(domains))
        self.assertEqual(domains[(1, 1)], {2})
        self.assertEqual(domains[(2, 2)], {2})

    def test_multi_cell_circle_propagation(self):
        constraint = ArrowConstraint(
            [(0, 0), (0, 1)],
            [(1, 0), (1, 1), (1, 2)],
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
            (1, 0): set(range(1, 10)),
            (1, 1): set(range(1, 10)),
            (1, 2): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        # Three shaft digits sum to at most 27, so the
        # circle's tens digit must be 1 or 2.
        self.assertEqual(domains[(0, 0)], {1, 2})

    def test_propagation_contradiction(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        domains = {
            (0, 0): {3},
            (0, 1): {2, 3},
            (0, 2): {2, 3},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_does_not_mutate_domains(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        domains = {
            (0, 0): {3},
            (0, 1): {2, 3},
            (0, 2): {2, 3},
        }

        snapshot = {
            cell: set(values)
            for cell, values in domains.items()
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

        self.assertEqual(domains, snapshot)

    def test_no_change_returns_false(self):
        constraint = ArrowConstraint(
            [(0, 0)],
            [(0, 1), (0, 2)],
        )

        domains = {
            (0, 0): {4},
            (0, 1): {1, 3},
            (0, 2): {1, 3},
        }

        self.assertFalse(
            constraint.propagate(domains)
        )

    def test_brute_force_single_circle(self):
        cells = [(0, 0), (0, 1), (0, 2)]
        constraint = ArrowConstraint([cells[0]], cells[1:])

        domains = {
            (0, 0): {4, 5, 6, 9},
            (0, 1): {1, 2, 8},
            (0, 2): {3, 4, 7},
        }

        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            if values[0] == values[1] + values[2]:
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

    def test_brute_force_multi_cell_circle(self):
        circle = [(0, 0), (0, 1)]
        shaft = [(1, 0), (1, 1), (1, 2)]
        cells = circle + shaft

        constraint = ArrowConstraint(circle, shaft)

        domains = {
            (0, 0): {1, 2},
            (0, 1): {2, 4, 8},
            (1, 0): {3, 5, 9},
            (1, 1): {4, 6},
            (1, 2): {5, 7, 9},
        }

        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            number = values[0] * 10 + values[1]

            if number == sum(values[2:]):
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

    def test_long_arrow_large_sums(self):
        circle = [(0, 0), (0, 1)]
        shaft = [(1, c) for c in range(8)]

        constraint = ArrowConstraint(circle, shaft)

        domains = {
            cell: set(range(1, 10))
            for cell in circle + shaft
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        # Eight shaft digits sum to 8..72, so the tens
        # digit of the circle is at most 7.
        self.assertEqual(domains[(0, 0)], set(range(1, 8)))

        # Every shaft digit keeps full support.
        for cell in shaft:
            self.assertEqual(domains[cell], set(range(1, 10)))

    def test_long_arrow_propagation_is_fast(self):
        circle = [(0, 0), (0, 1)]
        shaft = [(1, c) for c in range(9)] + [(2, 8), (3, 8)]

        constraint = ArrowConstraint(circle, shaft)

        domains = {
            cell: set(range(1, 10))
            for cell in circle + shaft
        }

        start = time.perf_counter()
        constraint.propagate(domains)
        elapsed = time.perf_counter() - start

        self.assertLess(
            elapsed, 1.0,
            f"Propagation took {elapsed:.3f}s"
        )


class TestArrowIntegration(unittest.TestCase):

    def test_constraint_registration(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 1
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            ArrowConstraint
        )

    def test_bent_shaft_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_arrow(
            [(2, 2)],
            [(3, 2), (4, 1), (5, 0), (6, 1)],
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            ArrowConstraint
        )

    def test_overlapping_arrows_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_arrow([(0, 5)], [(1, 6), (2, 6)])
        puzzle.add_arrow([(0, 7)], [(1, 6), (2, 5)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2
        )

    def test_disconnected_shaft_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([(0, 0)], [(0, 1), (0, 3)])

    def test_shaft_not_touching_circle_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([(0, 0)], [(5, 5), (5, 6)])

    def test_disconnected_circle_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow(
                [(0, 0), (0, 2)],
                [(0, 3), (0, 4)],
            )

    def test_repeated_cells_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([(0, 0)], [(0, 1), (0, 0)])

    def test_out_of_bounds_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([(0, 9)], [(1, 8)])

    def test_empty_sequences_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([], [(0, 0)])

        with self.assertRaises(ValueError):
            puzzle.add_arrow([(0, 0)], [])

    def test_solver_interaction(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        self.assertEqual(
            solution[(0, 0)],
            solution[(0, 1)] + solution[(0, 2)],
        )

        errors = validate_solution(puzzle, solution)

        self.assertEqual(errors, [])


class TestArrowValidation(unittest.TestCase):

    def test_validator_accepts_valid_arrow(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C7 = 9 and R2C6 + R3C5 = 5 + 4 = 9.
        puzzle.add_arrow([(0, 6)], [(1, 5), (2, 4)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_violation(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C1 = 5, but R1C2 + R1C3 = 3 + 4 = 7.
        puzzle.add_arrow([(0, 0)], [(0, 1), (0, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Arrow violation: circle [R1C1] expects 5, "
                "but the shaft sums to 7" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete_arrow(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_arrow([(0, 6)], [(1, 5), (2, 4)])

        solution = solved_assignment()
        del solution[(1, 5)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Arrow is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
