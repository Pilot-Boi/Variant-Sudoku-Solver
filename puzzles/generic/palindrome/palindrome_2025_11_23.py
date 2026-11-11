"""PuzzleMadness Palindrome Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [1, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 6, 4],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 1), (3, 0), (4, 0), (5, 1), (6, 2), (6, 3), (7, 4), (7, 3)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 7), (3, 6), (3, 7)])
    puzzle.add_palindrome([(8, 4), (8, 5), (7, 5), (6, 6), (6, 7)])
    puzzle.add_palindrome([(4, 3), (5, 4), (6, 5), (6, 4)])
    puzzle.add_palindrome([(5, 6), (5, 5), (4, 4)])

    return puzzle
