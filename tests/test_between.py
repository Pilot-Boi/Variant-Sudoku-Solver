import time
import unittest
from itertools import product

from sudoku.constraints import BetweenLineConstraint
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


class TestBetweenLineConstraint(unittest.TestCase):

    def test_valid_complete_assignment(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 2,
                (0, 1): 5,
                (0, 2): 3,
                (0, 3): 8,
            })
        )

    def test_endpoint_order_does_not_matter(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 8,
                (0, 1): 5,
                (0, 2): 2,
            })
        )

    def test_invalid_interior_value(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 2,
                (0, 1): 8,
                (0, 2): 8,
            })
        )

        # Equal to an endpoint is not strictly between.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 2,
                (0, 1): 2,
                (0, 2): 8,
            })
        )

    def test_repeated_interior_digits_allowed(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1,
                (1, 1): 5,
                (2, 2): 5,
                (3, 3): 9,
            })
        )

    def test_partial_assignment_valid(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # Interior 5 can sit between some endpoints.
        self.assertTrue(
            constraint.is_satisfied({(0, 1): 5})
        )

    def test_partial_assignment_contradiction(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # Endpoint 9 with interior 9: nothing is
        # strictly between any pairing.
        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 9,
                (0, 1): 9,
            })
        )

    def test_too_few_cells_rejected(self):
        with self.assertRaises(ValueError):
            BetweenLineConstraint([(0, 0), (0, 1)])

    def test_duplicate_cells_rejected(self):
        with self.assertRaises(ValueError):
            BetweenLineConstraint(
                [(0, 0), (0, 1), (0, 0)]
            )


class TestBetweenLinePropagation(unittest.TestCase):

    def test_endpoints_cannot_be_middle_values(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
            (0, 2): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        # Every endpoint value keeps a partner two away,
        # so endpoints stay full; interior digits need
        # strictly smaller and larger endpoint values.
        self.assertEqual(domains[(0, 0)], set(range(1, 10)))
        self.assertEqual(domains[(0, 1)], set(range(2, 9)))

    def test_fixed_endpoints_restrict_interior(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        domains = {
            (0, 0): {2},
            (0, 1): set(range(1, 10)),
            (0, 2): set(range(1, 10)),
            (0, 3): {8},
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 1)], {3, 4, 5, 6, 7})
        self.assertEqual(domains[(0, 2)], {3, 4, 5, 6, 7})

    def test_interior_restricts_endpoints(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): {5},
            (0, 2): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        # One endpoint below 5, the other above.
        self.assertEqual(
            domains[(0, 0)],
            {1, 2, 3, 4, 6, 7, 8, 9}
        )
        self.assertEqual(
            domains[(0, 2)],
            {1, 2, 3, 4, 6, 7, 8, 9}
        )

    def test_contradiction_raises(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        # Endpoint spans of at most 1 leave no room
        # for any interior digit.
        domains = {
            (0, 0): {5},
            (0, 1): set(range(1, 10)),
            (0, 2): {5, 6},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_does_not_mutate_domains(self):
        constraint = BetweenLineConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {5},
            (0, 1): {7, 8},
            (0, 2): {6},
        }

        snapshot = {
            cell: set(values)
            for cell, values in domains.items()
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

        self.assertEqual(domains, snapshot)

    def test_brute_force_supported_values(self):
        cells = [(0, 0), (0, 1), (0, 2), (0, 3)]
        constraint = BetweenLineConstraint(cells)

        domains = {
            (0, 0): {2, 5, 8},
            (0, 1): {1, 4, 6},
            (0, 2): {3, 6, 9},
            (0, 3): {4, 7},
        }

        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            low, high = sorted((values[0], values[-1]))

            if all(low < v < high for v in values[1:-1]):
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

    def test_long_line_propagation_is_fast(self):
        cells = [(0, c) for c in range(9)] + [(1, 8)]
        constraint = BetweenLineConstraint(cells)

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


class TestBetweenLineIntegration(unittest.TestCase):

    def test_registration(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_between_line([(0, 0), (1, 1), (2, 2)])

        self.assertEqual(
            len(puzzle.constraints), baseline + 1
        )

    def test_bent_and_overlapping_lines(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_between_line(
            [(5, 1), (6, 2), (6, 3), (7, 4)]
        )
        puzzle.add_between_line(
            [(8, 1), (7, 2), (6, 3), (5, 4)]
        )

        self.assertEqual(
            len(puzzle.constraints), baseline + 2
        )

    def test_non_adjacent_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_between_line(
                [(0, 0), (0, 2), (0, 3)]
            )

    def test_too_few_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_between_line([(0, 0), (0, 1)])

    def test_repeated_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_between_line(
                [(0, 0), (0, 1), (0, 0)]
            )

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_between_line(
                [(8, 7), (8, 8), (8, 9)]
            )

    def test_solver_integration(self):
        puzzle = empty_puzzle()

        puzzle.add_between_line(
            [(1, 1), (1, 2), (1, 3), (1, 4)]
        )

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        low, high = sorted(
            (solution[(1, 1)], solution[(1, 4)])
        )

        for cell in ((1, 2), (1, 3)):
            self.assertTrue(low < solution[cell] < high)

        self.assertEqual(
            validate_solution(puzzle, solution), []
        )


class TestBetweenLineValidation(unittest.TestCase):

    def test_validator_accepts_valid_line(self):
        puzzle = empty_puzzle()

        # 5, 7, 8: interior 7 lies between 5 and 8.
        puzzle.add_between_line([(0, 0), (1, 1), (2, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_violation(self):
        puzzle = empty_puzzle()

        # 5, 3, 4: interior 3 is not between 4 and 5.
        puzzle.add_between_line([(0, 0), (0, 1), (0, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Between Line violation: R1C2 = 3" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete(self):
        puzzle = empty_puzzle()
        puzzle.add_between_line([(0, 0), (1, 1), (2, 2)])

        solution = solved_assignment()
        del solution[(1, 1)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Between Line is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
