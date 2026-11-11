"""PuzzleMadness Palindrome Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 4],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 4, 3, 0, 9, 6],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 9, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 3), (4, 4), (3, 5), (3, 4), (2, 3), (2, 4), (1, 5), (0, 5)])
    puzzle.add_palindrome([(4, 5), (5, 4), (5, 3), (4, 2), (4, 1), (5, 2)])
    puzzle.add_palindrome([(1, 8), (2, 7), (2, 6), (3, 6), (4, 6)])
    puzzle.add_palindrome([(2, 1), (1, 2), (0, 3)])
    puzzle.add_palindrome([(8, 2), (7, 2), (6, 3)])

    return puzzle
