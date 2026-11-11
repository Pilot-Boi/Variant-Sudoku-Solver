"""PuzzleMadness Palindrome Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 5, 3, 6, 0, 0, 0, 0, 0],
        [0, 2, 4, 1, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (5, 2), (4, 1), (3, 2), (2, 1), (2, 0), (1, 0), (0, 1)])
    puzzle.add_palindrome([(7, 4), (6, 5), (5, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (6, 8)])
    puzzle.add_palindrome([(0, 2), (1, 2), (2, 3), (2, 4)])
    puzzle.add_palindrome([(1, 4), (1, 5), (2, 6), (2, 7)])

    return puzzle
