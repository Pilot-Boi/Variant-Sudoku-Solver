"""PuzzleMadness Palindrome Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 3, 0, 0, 0, 0, 4],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 5, 4, 0, 6, 0, 0, 3],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (4, 1), (3, 0), (3, 1), (2, 2), (1, 2), (0, 2), (1, 1)])
    puzzle.add_palindrome([(4, 4), (4, 3), (4, 2), (3, 2), (2, 3)])
    puzzle.add_palindrome([(6, 2), (7, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(7, 6), (7, 5), (6, 4), (5, 3), (5, 4)])
    puzzle.add_palindrome([(0, 7), (1, 6), (1, 5)])
    puzzle.add_palindrome([(5, 7), (5, 6), (4, 5)])

    return puzzle
