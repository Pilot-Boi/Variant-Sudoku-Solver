"""PuzzleMadness Palindrome Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 5, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 3, 0],
        [8, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 4, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 6, 4, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 3), (6, 4), (5, 4), (6, 5), (5, 5), (4, 5), (4, 4)])
    puzzle.add_palindrome([(1, 4), (2, 4), (3, 3), (4, 2), (5, 3), (5, 2)])
    puzzle.add_palindrome([(7, 8), (6, 8), (6, 7), (5, 7), (4, 7)])
    puzzle.add_palindrome([(1, 3), (2, 3), (3, 2), (2, 2)])
    puzzle.add_palindrome([(1, 5), (0, 5), (1, 6), (2, 7)])

    return puzzle
