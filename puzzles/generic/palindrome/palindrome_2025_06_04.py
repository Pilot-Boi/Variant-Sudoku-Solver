"""PuzzleMadness Palindrome Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [5, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 8), (7, 8), (6, 8), (5, 7), (4, 7), (3, 6), (4, 6)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 8), (3, 7), (4, 8), (3, 8)])
    puzzle.add_palindrome([(5, 2), (4, 1), (5, 0), (6, 0), (7, 0)])
    puzzle.add_palindrome([(2, 2), (3, 3), (2, 4), (1, 3)])
    puzzle.add_palindrome([(7, 1), (8, 2), (7, 3), (6, 3)])

    return puzzle
