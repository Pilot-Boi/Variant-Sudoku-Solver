"""PuzzleMadness Palindrome Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 7, 8, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 6, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 7, 8, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 2), (1, 2), (1, 3), (2, 2), (3, 1), (3, 2), (2, 3), (1, 4)])
    puzzle.add_palindrome([(5, 6), (5, 7), (4, 6), (3, 5), (4, 4), (3, 4)])
    puzzle.add_palindrome([(6, 1), (7, 2), (6, 3), (5, 4), (6, 4), (5, 5)])
    puzzle.add_palindrome([(4, 8), (3, 8), (3, 7), (2, 6), (2, 5)])
    puzzle.add_palindrome([(4, 1), (4, 2), (5, 3)])
    puzzle.add_palindrome([(1, 7), (1, 6), (0, 5), (0, 4)])

    return puzzle
