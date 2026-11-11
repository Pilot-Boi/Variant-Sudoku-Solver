"""PuzzleMadness Palindrome Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 9, 0, 6, 0, 0],
        [0, 0, 0, 5, 2, 0, 0, 0, 0],
        [0, 8, 0, 0, 1, 0, 4, 0, 0],
        [0, 0, 0, 0, 8, 0, 5, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 5), (6, 4), (7, 3), (8, 2), (7, 1), (6, 0)])
    puzzle.add_palindrome([(6, 2), (6, 3), (5, 4), (4, 4), (4, 5)])
    puzzle.add_palindrome([(7, 8), (6, 7), (6, 6), (5, 7), (4, 6), (3, 6)])
    puzzle.add_palindrome([(2, 3), (3, 2), (2, 1), (2, 0), (3, 1)])
    puzzle.add_palindrome([(2, 5), (1, 5), (0, 6)])
    puzzle.add_palindrome([(4, 3), (3, 3), (2, 4)])
    puzzle.add_palindrome([(1, 2), (0, 3), (0, 4)])

    return puzzle
