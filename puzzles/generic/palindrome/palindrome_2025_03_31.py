"""PuzzleMadness Palindrome Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [9, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 8, 0, 9, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 2, 0, 8, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 5, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 8), (6, 7), (6, 6), (7, 6), (8, 5), (8, 4), (7, 5)])
    puzzle.add_palindrome([(7, 3), (6, 2), (5, 2), (4, 1), (5, 1)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 6), (1, 5), (2, 4), (1, 3)])
    puzzle.add_palindrome([(8, 3), (7, 2), (6, 1)])
    puzzle.add_palindrome([(4, 6), (5, 6), (4, 5), (5, 4)])

    return puzzle
