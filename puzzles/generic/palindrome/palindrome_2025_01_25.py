"""PuzzleMadness Palindrome Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 5, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [9, 0, 0, 0, 4, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 9, 0, 6, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 1), (3, 2), (2, 3), (1, 3), (1, 2), (2, 1), (2, 0)])
    puzzle.add_palindrome([(1, 8), (1, 7), (0, 6), (1, 5), (2, 5), (2, 4)])
    puzzle.add_palindrome([(8, 1), (7, 2), (7, 3), (6, 4), (7, 4)])
    puzzle.add_palindrome([(4, 2), (5, 3), (5, 4)])
    puzzle.add_palindrome([(3, 8), (2, 7), (3, 6), (2, 6)])

    return puzzle
