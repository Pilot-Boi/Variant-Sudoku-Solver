import unittest

from sudoku.constraints import (
    XVConstraint,
    NegativeXVConstraint,
    generate_orthogonal_pairs,
)
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


class TestXVConstraint(unittest.TestCase):

    def test_v_marker_valid(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 3})
        )

    def test_v_marker_invalid(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 4})
        )

    def test_x_marker_valid(self):
        constraint = XVConstraint((0, 0), (0, 1), "X")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 6, (0, 1): 4})
        )

    def test_x_marker_invalid(self):
        constraint = XVConstraint((0, 0), (0, 1), "X")

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 6, (0, 1): 5})
        )

    def test_partial_assignment(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        self.assertTrue(constraint.is_satisfied({}))
        self.assertTrue(
            constraint.is_satisfied({(0, 0): 1})
        )

    def test_invalid_marker_rejected(self):
        with self.assertRaises(ValueError):
            XVConstraint((0, 0), (0, 1), "W")


class TestXVPropagation(unittest.TestCase):

    def test_v_propagation(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 0)], {1, 2, 3, 4})
        self.assertEqual(domains[(0, 1)], {1, 2, 3, 4})

    def test_x_propagation(self):
        constraint = XVConstraint((0, 0), (0, 1), "X")

        domains = {
            (0, 0): {1, 2, 3},
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 0)], {1, 2, 3})
        self.assertEqual(domains[(0, 1)], {7, 8, 9})

    def test_contradiction_raises(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        domains = {
            (0, 0): {5, 6},
            (0, 1): {5, 6},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_no_change_returns_false(self):
        constraint = XVConstraint((0, 0), (0, 1), "V")

        domains = {
            (0, 0): {2, 3},
            (0, 1): {2, 3},
        }

        self.assertFalse(constraint.propagate(domains))

    def test_brute_force_arc_consistency(self):
        constraint = XVConstraint((0, 0), (0, 1), "X")

        domains = {
            (0, 0): {1, 3, 5, 8},
            (0, 1): {2, 5, 7, 9},
        }

        supported_a = {
            x for x in domains[(0, 0)]
            if any(x + y == 10 for y in domains[(0, 1)])
        }
        supported_b = {
            y for y in domains[(0, 1)]
            if any(x + y == 10 for x in domains[(0, 0)])
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 0)], supported_a)
        self.assertEqual(domains[(0, 1)], supported_b)


class TestNegativeXVConstraint(unittest.TestCase):

    def test_rejects_sum_of_five(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 3})
        )

    def test_rejects_sum_of_ten(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 6, (0, 1): 4})
        )

    def test_accepts_other_sums(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 2, (0, 1): 2})
        )

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 9, (0, 1): 8})
        )

    def test_propagation(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {5},
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        # 5 + 5 = 10 is forbidden; 5 + y = 5 needs y = 0.
        self.assertEqual(
            domains[(0, 1)],
            {1, 2, 3, 4, 6, 7, 8, 9}
        )

    def test_contradiction_raises(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {5},
            (0, 1): {5},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_brute_force_arc_consistency(self):
        constraint = NegativeXVConstraint((0, 0), (0, 1))

        domains = {
            (0, 0): {1, 4, 6},
            (0, 1): {4, 6, 9},
        }

        def allowed(x, y):
            return x + y != 5 and x + y != 10

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


class TestXVPuzzleIntegration(unittest.TestCase):

    def test_add_xv(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_xv((0, 0), (0, 1), "V")
        puzzle.add_xv((3, 4), (4, 4), "X")

        self.assertEqual(
            len(puzzle.constraints), baseline + 2
        )

    def test_invalid_marker_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 0), (0, 1), "Y")

    def test_diagonal_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 0), (1, 1), "V")

    def test_nonadjacent_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 0), (0, 2), "X")

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 8), (0, 9), "V")

    def test_duplicate_marker_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_xv((0, 0), (0, 1), "V")

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 0), (0, 1), "V")

    def test_conflicting_marker_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_xv((0, 0), (0, 1), "V")

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 1), (0, 0), "X")

    def test_negative_constraints_exclude_markers(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_xv((0, 0), (0, 1), "V")
        puzzle.add_xv((5, 5), (6, 5), "X")

        puzzle.add_negative_xv_constraints()

        negative = [
            c for c in puzzle.constraints
            if isinstance(c, NegativeXVConstraint)
        ]

        self.assertEqual(len(generate_orthogonal_pairs()), 144)
        self.assertEqual(len(negative), 142)

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2 + 142
        )

    def test_negative_constraints_idempotent(self):
        puzzle = empty_puzzle()

        puzzle.add_negative_xv_constraints()
        count = len(puzzle.constraints)

        puzzle.add_negative_xv_constraints()

        self.assertEqual(len(puzzle.constraints), count)

    def test_marker_after_negative_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_negative_xv_constraints()

        with self.assertRaises(ValueError):
            puzzle.add_xv((0, 0), (0, 1), "V")

    def test_no_accidental_negative_constraints(self):
        puzzle = empty_puzzle()
        puzzle.add_xv((0, 0), (0, 1), "V")

        self.assertFalse(
            any(
                isinstance(c, NegativeXVConstraint)
                for c in puzzle.constraints
            )
        )

    def test_solver_integration(self):
        puzzle = empty_puzzle()

        puzzle.add_xv((0, 0), (0, 1), "V")
        puzzle.add_xv((4, 4), (5, 4), "X")

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        self.assertEqual(
            solution[(0, 0)] + solution[(0, 1)], 5
        )
        self.assertEqual(
            solution[(4, 4)] + solution[(5, 4)], 10
        )

        self.assertEqual(
            validate_solution(puzzle, solution), []
        )


class TestXVValidation(unittest.TestCase):

    def test_validator_accepts_valid_markers(self):
        puzzle = empty_puzzle()

        # R1C2 = 3 and R2C2 = 7 sum to 10.
        puzzle.add_xv((0, 1), (1, 1), "X")

        # R6C5 = 2 and R7C5 = 3 sum to 5.
        puzzle.add_xv((5, 4), (6, 4), "V")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_violation(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 and R1C2 = 3 sum to 8.
        puzzle.add_xv((0, 0), (0, 1), "V")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "XV violation: V marker requires R1C1 and "
                "R1C2 to sum to 5" in error
                for error in errors
            )
        )

    def test_validator_detects_negative_violation(self):
        puzzle = empty_puzzle()
        puzzle.add_negative_xv_constraints()

        # R1C2 = 3 and R2C2 = 7 sum to 10 while unmarked.
        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Negative XV violation: the unmarked pair "
                "R1C2 and R2C2" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete(self):
        puzzle = empty_puzzle()
        puzzle.add_xv((0, 1), (1, 1), "X")

        solution = solved_assignment()
        del solution[(0, 1)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "XV marker is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
