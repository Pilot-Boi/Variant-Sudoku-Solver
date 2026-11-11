"""PuzzleMadness Palindrome Sudoku — 2025-07-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 2, 5],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 2, 0, 1, 0, 0],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
    puzzle.add_palindrome([(1, 4), (2, 3), (3, 4), (4, 5), (3, 5)])
    puzzle.add_palindrome([(5, 2), (4, 2), (3, 1), (2, 0), (2, 1), (1, 0)])
    puzzle.add_palindrome([(7, 2), (6, 3), (6, 2), (5, 1), (5, 0)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 5)])
    puzzle.add_palindrome([(7, 5), (6, 5), (5, 4), (5, 3)])

    return puzzle
