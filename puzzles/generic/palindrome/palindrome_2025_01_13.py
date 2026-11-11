"""PuzzleMadness Palindrome Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 4, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 9, 0, 0, 6],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 5],
        [0, 0, 0, 0, 9, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 7), (7, 8), (6, 8), (5, 8), (5, 7), (5, 6), (6, 5)])
    puzzle.add_palindrome([(2, 8), (2, 7), (3, 7), (4, 8), (4, 7)])
    puzzle.add_palindrome([(2, 1), (2, 2), (1, 3), (0, 2), (0, 3), (0, 4)])
    puzzle.add_palindrome([(7, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(7, 5), (8, 5), (7, 6), (6, 7)])
    puzzle.add_palindrome([(2, 5), (2, 4), (3, 4)])

    return puzzle
