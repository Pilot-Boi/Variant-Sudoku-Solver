import unittest

from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution


VALID_GRID = [
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


def as_assignment(grid):
    return {
        (r, c): grid[r][c]
        for r in range(9)
        for c in range(9)
    }


class TestSolutionValidator(unittest.TestCase):

    def setUp(self):
        empty_grid = [[0] * 9 for _ in range(9)]
        self.puzzle = SudokuPuzzle(empty_grid)
        self.solution = as_assignment(VALID_GRID)

    def test_valid_standard_sudoku(self):
        self.assertEqual(
            validate_solution(self.puzzle, self.solution),
            []
        )

    def test_invalid_row(self):
        solution = self.solution.copy()
        solution[(0, 0)] = 3

        errors = validate_solution(self.puzzle, solution)

        self.assertTrue(
            any("Row 1" in error for error in errors)
        )

    def test_invalid_column(self):
        solution = self.solution.copy()
        solution[(0, 0)] = 6

        errors = validate_solution(self.puzzle, solution)

        self.assertTrue(
            any("Column 1" in error for error in errors)
        )

    def test_invalid_box(self):
        solution = self.solution.copy()
        solution[(0, 0)] = 7

        errors = validate_solution(self.puzzle, solution)

        self.assertTrue(
            any("Box 1" in error for error in errors)
        )

    def test_invalid_given(self):
        grid = [[0] * 9 for _ in range(9)]
        grid[0][0] = 9

        puzzle = SudokuPuzzle(grid)

        errors = validate_solution(puzzle, self.solution)

        self.assertTrue(
            any("Given digit mismatch" in error for error in errors)
        )

    def test_valid_thermometer(self):
        # R1C2=3, R1C3=4, R1C4=6
        self.puzzle.add_thermometer([
            (0, 1), (0, 2), (0, 3)
        ])

        self.assertEqual(
            validate_solution(self.puzzle, self.solution),
            []
        )

    def test_invalid_thermometer(self):
        # R1C4=6, R1C3=4, R1C2=3: decreasing
        self.puzzle.add_thermometer([
            (0, 3), (0, 2), (0, 1)
        ])

        errors = validate_solution(self.puzzle, self.solution)

        self.assertTrue(
            any("Invalid thermometer" in error for error in errors)
        )

    def test_valid_killer_cage(self):
        # R1C1=5, R1C2=3, sum=8
        self.puzzle.add_killer_cage([
            (0, 0), (0, 1)
        ], 8)

        self.assertEqual(
            validate_solution(self.puzzle, self.solution),
            []
        )

    def test_invalid_killer_sum(self):
        self.puzzle.add_killer_cage([
            (0, 0), (0, 1)
        ], 9)

        errors = validate_solution(self.puzzle, self.solution)

        self.assertTrue(
            any("Invalid Killer cage" in error for error in errors)
        )

    def test_invalid_killer_duplicate(self):
        # Two 5s, sum 10: sum is correct but repetition is not.
        self.puzzle.add_killer_cage([
            (0, 0), (1, 5)
        ], 10)

        errors = validate_solution(self.puzzle, self.solution)

        self.assertTrue(
            any("Invalid Killer cage" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()