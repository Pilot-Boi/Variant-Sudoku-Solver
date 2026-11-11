"""PuzzleMadness Palindrome Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [6, 0, 0, 0, 0, 0, 7, 0, 3],
        [0, 0, 2, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 9, 0, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (6, 4), (6, 3), (6, 2), (7, 3), (8, 2), (8, 1), (8, 0)])
    puzzle.add_palindrome([(5, 0), (4, 1), (5, 2), (4, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(1, 1), (2, 2), (2, 3), (1, 3), (0, 4)])
    puzzle.add_palindrome([(2, 1), (3, 1), (4, 0)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 5), (7, 6)])

    return puzzle
