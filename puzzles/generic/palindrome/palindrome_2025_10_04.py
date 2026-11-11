"""PuzzleMadness Palindrome Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 6],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 0, 0],
        [8, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 2, 4, 0, 0],
        [0, 7, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 9, 5, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 7), (1, 6), (2, 5), (3, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_palindrome([(6, 2), (7, 2), (6, 1), (5, 2), (6, 3), (5, 4)])
    puzzle.add_palindrome([(5, 7), (4, 6), (5, 6), (6, 7), (7, 7), (8, 8)])
    puzzle.add_palindrome([(1, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(8, 7), (7, 6), (6, 5)])

    return puzzle
