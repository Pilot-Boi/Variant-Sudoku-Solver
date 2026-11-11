"""PuzzleMadness Palindrome Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 9, 0, 4, 0],
        [1, 0, 0, 0, 0, 5, 0, 2, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 5, 0],
        [0, 5, 0, 0, 0, 1, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 0), (2, 1), (2, 0), (3, 1), (4, 1), (3, 2), (4, 3)])
    puzzle.add_palindrome([(1, 4), (2, 4), (3, 4), (2, 5), (3, 6), (3, 5)])
    puzzle.add_palindrome([(5, 2), (5, 1), (4, 2), (5, 3), (6, 2), (7, 3)])
    puzzle.add_palindrome([(4, 5), (5, 4), (6, 3), (7, 4)])
    puzzle.add_palindrome([(1, 2), (1, 3), (2, 2), (3, 3)])

    return puzzle
