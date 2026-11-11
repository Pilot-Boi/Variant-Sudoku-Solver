"""PuzzleMadness Palindrome Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [6, 9, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 0, 0, 0, 3, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 7],
        [1, 0, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (4, 3), (4, 2), (5, 1), (6, 0), (7, 1), (8, 1), (7, 0)])
    puzzle.add_palindrome([(7, 3), (6, 4), (5, 3), (5, 2), (6, 2)])
    puzzle.add_palindrome([(4, 1), (3, 2), (2, 1), (1, 1), (1, 2)])
    puzzle.add_palindrome([(2, 4), (1, 5), (0, 6), (1, 6)])
    puzzle.add_palindrome([(8, 5), (7, 5), (6, 6), (6, 7)])

    return puzzle
