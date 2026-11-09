import unittest

from sudoku.constraints import ParityConstraint
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


class TestParityConstraint(unittest.TestCase):

    def test_odd_valid(self):
        constraint = ParityConstraint((0, 0), "odd")

        for value in (1, 3, 5, 7, 9):
            self.assertTrue(
                constraint.is_satisfied({(0, 0): value})
            )

    def test_odd_invalid(self):
        constraint = ParityConstraint((0, 0), "odd")

        for value in (2, 4, 6, 8):
            self.assertFalse(
                constraint.is_satisfied({(0, 0): value})
            )

    def test_even_valid(self):
        constraint = ParityConstraint((0, 0), "even")

        for value in (2, 4, 6, 8):
            self.assertTrue(
                constraint.is_satisfied({(0, 0): value})
            )

    def test_even_invalid(self):
        constraint = ParityConstraint((0, 0), "even")

        for value in (1, 3, 5, 7, 9):
            self.assertFalse(
                constraint.is_satisfied({(0, 0): value})
            )

    def test_partial_assignment(self):
        constraint = ParityConstraint((0, 0), "odd")

        self.assertTrue(constraint.is_satisfied({}))

    def test_invalid_parity_rejected(self):
        with self.assertRaises(ValueError):
            ParityConstraint((0, 0), "prime")


class TestParityPropagation(unittest.TestCase):

    def test_odd_propagation(self):
        constraint = ParityConstraint((0, 0), "odd")

        domains = {(0, 0): set(range(1, 10))}

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 0)], {1, 3, 5, 7, 9})

    def test_even_propagation(self):
        constraint = ParityConstraint((0, 0), "even")

        domains = {(0, 0): set(range(1, 10))}

        self.assertTrue(constraint.propagate(domains))
        self.assertEqual(domains[(0, 0)], {2, 4, 6, 8})

    def test_contradiction_raises(self):
        constraint = ParityConstraint((0, 0), "even")

        domains = {(0, 0): {1, 3, 5}}

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_no_change_returns_false(self):
        constraint = ParityConstraint((0, 0), "odd")

        domains = {(0, 0): {1, 9}}

        self.assertFalse(constraint.propagate(domains))


class TestParityIntegration(unittest.TestCase):

    def test_registration(self):
        puzzle = empty_puzzle()
        baseline = len(puzzle.constraints)

        puzzle.add_odd_cell((0, 0))
        puzzle.add_even_cell((0, 1))

        self.assertEqual(
            len(puzzle.constraints), baseline + 2
        )

    def test_out_of_bounds_rejected(self):
        puzzle = empty_puzzle()

        with self.assertRaises(ValueError):
            puzzle.add_odd_cell((9, 0))

        with self.assertRaises(ValueError):
            puzzle.add_even_cell((-1, 0))

    def test_duplicate_registration_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_odd_cell((0, 0))

        with self.assertRaises(ValueError):
            puzzle.add_odd_cell((0, 0))

    def test_conflicting_parity_rejected(self):
        puzzle = empty_puzzle()
        puzzle.add_odd_cell((0, 0))

        with self.assertRaises(ValueError):
            puzzle.add_even_cell((0, 0))

    def test_solver_integration(self):
        puzzle = empty_puzzle()

        puzzle.add_odd_cell((0, 0))
        puzzle.add_even_cell((0, 1))
        puzzle.add_even_cell((8, 8))

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(solution[(0, 0)] % 2, 1)
        self.assertEqual(solution[(0, 1)] % 2, 0)
        self.assertEqual(solution[(8, 8)] % 2, 0)

        self.assertEqual(
            validate_solution(puzzle, solution), []
        )

    def test_mixed_variants(self):
        puzzle = empty_puzzle()

        puzzle.add_odd_cell((4, 4))
        puzzle.add_xv((0, 0), (0, 1), "V")
        puzzle.add_between_line([(6, 1), (6, 2), (6, 3)])

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(
            validate_solution(puzzle, solution), []
        )


class TestParityValidation(unittest.TestCase):

    def test_validator_accepts_valid_parities(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 is odd; R1C6 = 8 is even.
        puzzle.add_odd_cell((0, 0))
        puzzle.add_even_cell((0, 5))

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_odd_violation(self):
        puzzle = empty_puzzle()

        # R1C6 = 8 is even, not odd.
        puzzle.add_odd_cell((0, 5))

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Parity violation: R1C6 must contain an "
                "odd digit" in error
                for error in errors
            )
        )

    def test_validator_detects_even_violation(self):
        puzzle = empty_puzzle()

        # R1C1 = 5 is odd, not even.
        puzzle.add_even_cell((0, 0))

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Parity violation: R1C1 must contain an "
                "even digit" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete(self):
        puzzle = empty_puzzle()
        puzzle.add_odd_cell((0, 0))

        solution = solved_assignment()
        del solution[(0, 0)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Parity cell is incomplete" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
