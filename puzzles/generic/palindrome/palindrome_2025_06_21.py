"""PuzzleMadness Palindrome Sudoku — 2025-06-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 4, 2, 0, 0, 0, 0, 8],
        [5, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 9, 0],
        [0, 0, 0, 8, 0, 0, 0, 7, 0],
        [0, 6, 0, 1, 0, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (1, 3), (2, 4), (3, 5), (4, 6), (4, 5), (5, 5), (4, 4)])
    puzzle.add_palindrome([(1, 7), (1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(4, 1), (4, 0), (5, 1), (6, 2), (5, 3)])
    puzzle.add_palindrome([(8, 4), (7, 4), (8, 5), (7, 6), (6, 7), (7, 8)])
    puzzle.add_palindrome([(4, 7), (5, 6), (6, 6)])
    puzzle.add_palindrome([(4, 2), (4, 3), (3, 2), (2, 1)])

    return puzzle
