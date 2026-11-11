"""PuzzleMadness Palindrome Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 3, 9],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 6, 1, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 7, 0, 0],
        [0, 0, 7, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 7), (4, 6), (3, 6), (3, 5), (2, 4), (1, 5), (2, 5)])
    puzzle.add_palindrome([(8, 0), (7, 0), (6, 0), (5, 1), (4, 2), (4, 1)])
    puzzle.add_palindrome([(8, 1), (8, 2), (8, 3), (7, 4), (6, 5)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7)])
    puzzle.add_palindrome([(3, 4), (4, 3), (3, 2), (2, 2)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 5), (1, 4)])

    return puzzle
