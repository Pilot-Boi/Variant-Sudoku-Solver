"""PuzzleMadness Palindrome Sudoku — 2025-08-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 7, 0, 0, 1, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 4, 8, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 0), (2, 1), (1, 2), (2, 2), (3, 3), (3, 4), (4, 4), (5, 4)])
    puzzle.add_palindrome([(4, 2), (5, 2), (5, 3), (6, 4), (7, 4), (6, 5)])
    puzzle.add_palindrome([(0, 0), (0, 1), (0, 2), (1, 3), (1, 4)])
    puzzle.add_palindrome([(8, 4), (8, 3), (8, 2), (7, 3), (6, 2), (5, 1)])
    puzzle.add_palindrome([(3, 6), (4, 6), (3, 5), (2, 5)])
    puzzle.add_palindrome([(5, 8), (6, 7), (6, 6)])

    return puzzle
