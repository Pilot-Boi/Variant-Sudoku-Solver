"""PuzzleMadness Palindrome Sudoku — 2025-08-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 3, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 1, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 4, 8],
        [0, 0, 8, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 7), (0, 7), (0, 6), (1, 6), (2, 5), (1, 4), (0, 3)])
    puzzle.add_palindrome([(1, 8), (2, 8), (3, 7), (3, 6), (4, 7)])
    puzzle.add_palindrome([(8, 1), (7, 0), (6, 1), (5, 2), (5, 3), (4, 2)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 8)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7)])

    return puzzle
