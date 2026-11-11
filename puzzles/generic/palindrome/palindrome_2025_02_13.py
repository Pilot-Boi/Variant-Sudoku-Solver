"""PuzzleMadness Palindrome Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 3, 0, 6, 0, 0, 0, 0, 0],
        [1, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 5, 0, 2, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 0, 0, 0],
        [8, 7, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 1), (1, 2), (0, 3), (1, 3), (2, 2), (3, 1), (4, 2)])
    puzzle.add_palindrome([(2, 5), (1, 6), (2, 7), (3, 8), (3, 7)])
    puzzle.add_palindrome([(8, 0), (7, 1), (6, 2), (5, 3), (5, 4), (6, 4)])
    puzzle.add_palindrome([(4, 7), (5, 7), (6, 6)])
    puzzle.add_palindrome([(6, 5), (5, 5), (4, 6)])

    return puzzle
