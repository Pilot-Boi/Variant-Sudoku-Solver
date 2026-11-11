"""PuzzleMadness Palindrome Sudoku — 2025-03-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 7, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 4, 0, 0, 5],
        [9, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 1), (5, 1), (5, 2), (4, 2), (3, 3), (4, 4), (3, 4)])
    puzzle.add_palindrome([(2, 1), (3, 2), (2, 2), (1, 3), (0, 3), (1, 4)])
    puzzle.add_palindrome([(4, 8), (3, 7), (3, 8), (2, 7), (2, 8), (1, 7)])
    puzzle.add_palindrome([(6, 6), (7, 5), (7, 4)])
    puzzle.add_palindrome([(7, 2), (8, 2), (7, 3), (8, 4)])

    return puzzle
