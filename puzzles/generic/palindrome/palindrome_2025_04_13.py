"""PuzzleMadness Palindrome Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 2, 0, 0, 0, 0, 0],
        [7, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 7],
        [0, 0, 0, 9, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [9, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 6), (2, 6), (1, 7), (1, 6), (0, 5), (1, 4), (2, 5)])
    puzzle.add_palindrome([(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (1, 3)])
    puzzle.add_palindrome([(5, 8), (6, 7), (6, 6), (5, 7), (4, 6), (3, 5)])
    puzzle.add_palindrome([(5, 2), (6, 2), (7, 3), (8, 3)])
    puzzle.add_palindrome([(4, 1), (3, 0), (2, 1), (2, 2)])
    puzzle.add_palindrome([(3, 2), (4, 2), (5, 3)])

    return puzzle
