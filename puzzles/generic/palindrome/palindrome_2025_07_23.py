"""PuzzleMadness Palindrome Sudoku — 2025-07-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 5, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 6, 9, 0, 0],
        [7, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 7), (7, 6), (7, 7), (6, 8), (5, 8), (4, 7), (3, 8)])
    puzzle.add_palindrome([(5, 2), (6, 3), (7, 2), (8, 3), (8, 2), (7, 1)])
    puzzle.add_palindrome([(4, 1), (3, 2), (4, 2), (4, 3), (5, 4)])
    puzzle.add_palindrome([(4, 6), (4, 5), (5, 5), (5, 6), (6, 7)])
    puzzle.add_palindrome([(2, 5), (3, 6), (3, 7)])
    puzzle.add_palindrome([(1, 2), (0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(2, 1), (3, 0), (4, 0)])

    return puzzle
