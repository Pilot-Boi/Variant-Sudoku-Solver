"""PuzzleMadness Palindrome Sudoku — 2025-08-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 7, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 9, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 3), (7, 3), (6, 4), (5, 3), (6, 2), (7, 1), (8, 1), (7, 0)])
    puzzle.add_palindrome([(1, 4), (2, 4), (1, 5), (2, 6), (3, 7), (2, 8)])
    puzzle.add_palindrome([(7, 5), (6, 6), (5, 5), (4, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(8, 4), (8, 5), (7, 6)])
    puzzle.add_palindrome([(5, 0), (5, 1), (6, 1)])

    return puzzle
