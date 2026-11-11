"""PuzzleMadness Palindrome Sudoku — 2025-10-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 3],
        [1, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 5],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 5), (7, 5), (6, 4), (5, 4), (6, 3), (5, 2), (5, 3), (4, 3)])
    puzzle.add_palindrome([(6, 8), (7, 7), (7, 6), (6, 5), (5, 6)])
    puzzle.add_palindrome([(4, 7), (3, 8), (2, 8), (2, 7), (1, 8)])
    puzzle.add_palindrome([(2, 2), (2, 3), (1, 4)])
    puzzle.add_palindrome([(4, 4), (3, 5), (2, 6), (1, 6)])
    puzzle.add_palindrome([(1, 1), (0, 2), (1, 3), (0, 3)])

    return puzzle
