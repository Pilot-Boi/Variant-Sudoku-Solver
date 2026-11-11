"""PuzzleMadness Palindrome Sudoku — 2025-12-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 9, 0, 7, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 7, 0],
        [0, 5, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 6, 0, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 1), (5, 0), (6, 0), (6, 1), (5, 2), (4, 2), (3, 3), (2, 4)])
    puzzle.add_palindrome([(6, 5), (6, 4), (7, 5), (6, 6), (7, 6), (8, 6)])
    puzzle.add_palindrome([(1, 7), (2, 7), (2, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 7), (6, 8)])
    puzzle.add_palindrome([(6, 2), (7, 2), (8, 3)])

    return puzzle
