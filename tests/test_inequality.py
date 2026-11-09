import unittest

from sudoku.constraints import InequalityConstraint
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


class TestInequalityConstraint(unittest.TestCase):

    def test_less_than_valid(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 3, (0, 1): 7})
        )

    def test_less_than_invalid(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 7, (0, 1): 3})
        )

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 5, (0, 1): 5})
        )

    def test_greater_than(self):
        constraint = InequalityConstraint((0, 0), (0, 1), ">")

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 7, (0, 1): 3})
        )

        self.assertFalse(
            constraint.is_satisfied({(0, 0): 3, (0, 1): 7})
        )

    def test_partial_assignment(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        self.assertTrue(constraint.is_satisfied({}))
        self.assertTrue(
            constraint.is_satisfied({(0, 0): 9})
        )

    def test_invalid_operator_rejected(self):
        with self.assertRaises(ValueError):
            InequalityConstraint((0, 0), (0, 1), "<=")

    def test_identical_cells_rejected(self):
        with self.assertRaises(ValueError):
            InequalityConstraint((0, 0), (0, 0), "<")


class TestInequalityPropagation(unittest.TestCase):

    def test_bidirectional_propagation(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        domains = {
            (0, 0): set(range(1, 10)),
            (0, 1): set(range(1, 10)),
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 0)], set(range(1, 9)))
        self.assertEqual(domains[(0, 1)], set(range(2, 10)))

    def test_tight_bounds(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        domains = {
            (0, 0): {5, 6, 7},
            (0, 1): {4, 5, 6},
        }

        self.assertTrue(constraint.propagate(domains))

        self.assertEqual(domains[(0, 0)], {5})
        self.assertEqual(domains[(0, 1)], {6})

    def test_contradiction_raises(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        domains = {
            (0, 0): {7, 8, 9},
            (0, 1): {1, 2, 3},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_no_change_returns_false(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        domains = {
            (0, 0): {1, 2},
            (0, 1): {8, 9},
        }

        self.assertFalse(constraint.propagate(domains))

    def test_brute_force_arc_consistency(self):
        constraint = InequalityConstraint((0, 0), (0, 1), "<")

        domains = {
            (0, 0): {2, 4, 6, 8},
            (0, 1): {1, 5, 7},
        }

        supported_a = {
            x for x in domains[(0, 0)]
            if any(x < y for y in domains[(0, 1)])
        }
        supported_b = {
            y for y in domains[(0, 1)]
            if any(x < y for x in domains[(0, 0)])
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 0)], supported_a)
        self.assertEqual(domains[(0, 1)], supported_b)


class TestInequalityIntegration(unittest.TestCase):

    def test_registration(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_inequality((0, 0), (0, 1), "<")

        self.assertEqual(
            len(puzzle.constraints), baseline + 1
        )

    def test_nonadjacent_cells_allowed(self):
        puzzle = empty_puzzle()

        puzzle.add_inequality((0, 0), (5, 7), "<")

        self.assertIsInstance(
            puzzle.constraints[-1],
            InequalityConstraint
        )

    def test_invalid_operator_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 0), (0, 1), "!=")

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 9), (0, 8), "<")

    def test_identical_cells_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 0), (0, 0), "<")

    def test_duplicate_definition_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_inequality((0, 0), (0, 1), "<")

        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 0), (0, 1), "<")

        # Same relation stated the other way around.
        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 1), (0, 0), ">")

    def test_conflicting_definition_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_inequality((0, 0), (0, 1), "<")

        with self.assertRaises(ValueError):
            puzzle.add_inequality((0, 0), (0, 1), ">")

    def test_solver_integration(self):
        puzzle = empty_puzzle()

        puzzle.add_inequality((0, 0), (0, 1), "<")
        puzzle.add_inequality((8, 8), (0, 0), ">")

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertLess(solution[(0, 0)], solution[(0, 1)])
        self.assertGreater(solution[(8, 8)], solution[(0, 0)])

        errors = validate_solution(puzzle, solution)

        self.assertEqual(errors, [])

    def test_mixed_variants(self):
        puzzle = empty_puzzle()

        puzzle.add_inequality((0, 0), (0, 1), "<")
        puzzle.add_kropki_dot((4, 4), (4, 5), "white")
        puzzle.add_odd_cell((8, 8))

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(
            validate_solution(puzzle, solution), []
        )


class TestInequalityValidation(unittest.TestCase):

    def test_validator_accepts_valid_inequality(self):
        puzzle = empty_puzzle()

        # R1C2 = 3 < R1C3 = 4.
        puzzle.add_inequality((0, 1), (0, 2), "<")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_violation(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 is not less than R1C2 = 3.
        puzzle.add_inequality((0, 0), (0, 1), "<")

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Inequality violation: R1C1 must be < R1C2"
                in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete(self):
        puzzle = empty_puzzle()
        puzzle.add_inequality((0, 1), (0, 2), "<")

        solution = solved_assignment()
        del solution[(0, 1)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Inequality is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
