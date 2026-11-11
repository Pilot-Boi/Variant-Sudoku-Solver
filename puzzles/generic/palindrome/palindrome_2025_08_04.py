"""PuzzleMadness Palindrome Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 6, 0, 0, 8],
        [0, 4, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (7, 4), (6, 3), (5, 4), (4, 4), (4, 5), (3, 4)])
    puzzle.add_palindrome([(8, 1), (7, 2), (6, 2), (5, 1), (4, 1), (5, 0)])
    puzzle.add_palindrome([(6, 6), (6, 7), (7, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_palindrome([(1, 4), (2, 5), (2, 6), (3, 5), (4, 6), (4, 7)])
    puzzle.add_palindrome([(4, 2), (3, 2), (2, 3), (1, 3)])
    puzzle.add_palindrome([(1, 7), (2, 8), (3, 8)])

    return puzzle
