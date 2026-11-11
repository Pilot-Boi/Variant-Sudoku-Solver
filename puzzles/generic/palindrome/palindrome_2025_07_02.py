"""PuzzleMadness Palindrome Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 5, 0],
        [2, 0, 0, 0, 0, 0, 1, 0, 0],
        [6, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 2, 7],
        [0, 2, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (5, 5), (5, 4), (5, 3), (6, 4), (7, 3), (7, 4), (7, 5)])
    puzzle.add_palindrome([(5, 2), (4, 1), (3, 2), (4, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(1, 7), (1, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (1, 4)])
    puzzle.add_palindrome([(2, 4), (3, 5), (2, 6), (3, 6)])

    return puzzle
