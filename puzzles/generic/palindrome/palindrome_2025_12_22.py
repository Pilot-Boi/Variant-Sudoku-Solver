"""PuzzleMadness Palindrome Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 2],
        [0, 4, 0, 0, 0, 0, 0, 0, 1],
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 0, 7],
        [0, 0, 4, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (4, 4), (5, 5), (6, 6), (7, 6), (7, 7), (8, 6)])
    puzzle.add_palindrome([(1, 7), (1, 6), (2, 6), (3, 5), (2, 5), (3, 4)])
    puzzle.add_palindrome([(0, 8), (0, 7), (0, 6), (1, 5), (2, 4), (1, 4)])
    puzzle.add_palindrome([(4, 2), (3, 1), (2, 0)])
    puzzle.add_palindrome([(4, 5), (3, 6), (2, 7)])
    puzzle.add_palindrome([(1, 1), (0, 2), (1, 3), (0, 3)])

    return puzzle
