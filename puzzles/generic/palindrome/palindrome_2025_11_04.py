"""PuzzleMadness Palindrome Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 5, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [3, 0, 0, 0, 2, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 8), (0, 7), (1, 8), (2, 7), (3, 8), (4, 7), (3, 6), (4, 6)])
    puzzle.add_palindrome([(4, 8), (5, 7), (5, 6), (4, 5), (5, 4)])
    puzzle.add_palindrome([(0, 5), (0, 4), (1, 3), (2, 2), (1, 1)])
    puzzle.add_palindrome([(8, 5), (7, 5), (6, 4), (5, 3), (4, 3)])
    puzzle.add_palindrome([(0, 3), (0, 2), (1, 2)])
    puzzle.add_palindrome([(4, 2), (3, 2), (2, 3), (3, 4)])

    return puzzle
