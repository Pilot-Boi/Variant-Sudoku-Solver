"""PuzzleMadness Palindrome Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 2, 5, 0],
        [0, 8, 0, 0, 5, 0, 0, 0, 0],
        [0, 2, 7, 0, 0, 0, 0, 0, 0],
        [0, 6, 3, 0, 0, 0, 0, 0, 0],
        [6, 3, 0, 0, 0, 1, 0, 0, 2],
        [1, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (7, 4), (6, 3), (7, 3), (8, 2), (7, 1), (8, 1), (8, 0)])
    puzzle.add_palindrome([(5, 7), (4, 8), (3, 7), (2, 7), (2, 8)])
    puzzle.add_palindrome([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)])
    puzzle.add_palindrome([(6, 4), (6, 5), (5, 6)])
    puzzle.add_palindrome([(2, 6), (3, 5), (4, 6), (5, 5)])

    return puzzle
