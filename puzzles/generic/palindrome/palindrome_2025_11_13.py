"""PuzzleMadness Palindrome Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 6, 0, 0, 0, 0, 0, 1],
        [0, 7, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 3), (4, 3), (5, 2), (5, 1), (6, 0), (6, 1), (7, 2), (8, 2)])
    puzzle.add_palindrome([(5, 6), (4, 5), (3, 6), (2, 7), (2, 8)])
    puzzle.add_palindrome([(6, 2), (7, 3), (6, 4), (5, 3), (5, 4), (5, 5)])
    puzzle.add_palindrome([(0, 7), (1, 7), (0, 6), (1, 5), (2, 4), (2, 3)])
    puzzle.add_palindrome([(1, 2), (1, 3), (0, 4)])
    puzzle.add_palindrome([(4, 8), (5, 7), (6, 7)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 1), (4, 0)])

    return puzzle
