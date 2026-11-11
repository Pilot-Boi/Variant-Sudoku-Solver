"""PuzzleMadness Palindrome Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [4, 0, 7, 0, 0, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 5, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (4, 3), (4, 4), (3, 4), (2, 3), (2, 2), (2, 1), (1, 0)])
    puzzle.add_palindrome([(5, 6), (5, 5), (5, 4), (6, 3), (6, 4)])
    puzzle.add_palindrome([(1, 8), (0, 7), (1, 6), (0, 5), (1, 5), (2, 4)])
    puzzle.add_palindrome([(2, 5), (2, 6), (1, 7)])
    puzzle.add_palindrome([(5, 8), (6, 8), (7, 7)])
    puzzle.add_palindrome([(4, 7), (3, 8), (2, 8)])

    return puzzle
