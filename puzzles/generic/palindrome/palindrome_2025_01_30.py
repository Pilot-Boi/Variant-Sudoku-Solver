"""PuzzleMadness Palindrome Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 8, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 3, 6, 0, 0, 0, 5, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [6, 0, 2, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 5), (2, 6), (2, 5), (3, 4), (4, 4), (5, 5), (4, 6)])
    puzzle.add_palindrome([(4, 2), (5, 3), (6, 4), (7, 4), (6, 5)])
    puzzle.add_palindrome([(5, 2), (6, 3), (6, 2), (7, 3), (8, 2), (8, 3)])
    puzzle.add_palindrome([(1, 7), (2, 8), (2, 7), (3, 6), (4, 7), (4, 8)])
    puzzle.add_palindrome([(2, 1), (3, 2), (3, 3)])
    puzzle.add_palindrome([(7, 6), (8, 6), (7, 5), (8, 4)])
    puzzle.add_palindrome([(1, 2), (1, 3), (0, 4)])

    return puzzle
