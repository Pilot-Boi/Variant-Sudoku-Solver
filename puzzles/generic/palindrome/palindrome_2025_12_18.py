"""PuzzleMadness Palindrome Sudoku — 2025-12-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 5, 0],
        [7, 0, 0, 0, 0, 4, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 2), (2, 3), (3, 4), (3, 3), (4, 2), (5, 1), (6, 2), (7, 3)])
    puzzle.add_palindrome([(1, 3), (0, 3), (1, 2), (2, 1), (2, 0)])
    puzzle.add_palindrome([(8, 3), (7, 4), (6, 4), (5, 3), (5, 4)])
    puzzle.add_palindrome([(2, 7), (1, 7), (2, 6), (1, 5), (0, 5), (1, 4)])
    puzzle.add_palindrome([(5, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(7, 6), (7, 5), (8, 4)])
    puzzle.add_palindrome([(2, 8), (3, 7), (3, 6)])

    return puzzle
