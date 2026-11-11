"""PuzzleMadness Palindrome Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 3],
        [4, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 1, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (5, 3), (6, 4), (5, 5), (4, 6), (3, 7), (3, 6)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 7), (3, 8), (4, 8)])
    puzzle.add_palindrome([(8, 8), (7, 8), (6, 8), (5, 7), (4, 7)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1), (6, 2), (7, 3), (8, 3)])
    puzzle.add_palindrome([(1, 3), (2, 2), (3, 1), (2, 0)])
    puzzle.add_palindrome([(2, 6), (1, 6), (2, 5), (3, 5)])
    puzzle.add_palindrome([(8, 4), (7, 5), (7, 6)])

    return puzzle
