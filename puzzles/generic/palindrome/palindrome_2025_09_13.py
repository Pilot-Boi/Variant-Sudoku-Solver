"""PuzzleMadness Palindrome Sudoku — 2025-09-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 1, 0, 4, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [2, 0, 0, 7, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 3, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 0, 5, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (5, 6), (4, 7), (3, 8), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_palindrome([(5, 4), (6, 5), (7, 5), (8, 6), (7, 7), (8, 7)])
    puzzle.add_palindrome([(6, 3), (5, 3), (4, 3), (3, 2), (3, 1)])
    puzzle.add_palindrome([(0, 6), (1, 6), (2, 6), (2, 5), (3, 4)])
    puzzle.add_palindrome([(5, 0), (5, 1), (6, 2)])
    puzzle.add_palindrome([(0, 3), (1, 3), (2, 2), (2, 1)])

    return puzzle
