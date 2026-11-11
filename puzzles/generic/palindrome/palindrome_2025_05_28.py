"""PuzzleMadness Palindrome Sudoku — 2025-05-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 8, 0, 0, 9, 0, 0],
        [3, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 1, 9],
        [0, 6, 0, 0, 0, 7, 0, 0, 8],
        [8, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (5, 4), (6, 3), (7, 2), (8, 1), (8, 0), (7, 1)])
    puzzle.add_palindrome([(2, 8), (2, 7), (1, 6), (0, 5), (0, 4), (1, 4)])
    puzzle.add_palindrome([(2, 5), (2, 4), (1, 3), (0, 2), (1, 2), (1, 1)])
    puzzle.add_palindrome([(5, 6), (6, 6), (7, 5)])
    puzzle.add_palindrome([(5, 2), (5, 1), (6, 0), (7, 0)])

    return puzzle
