"""PuzzleMadness Palindrome Sudoku — 2025-11-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 9, 0, 8, 0, 2],
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 1), (5, 2), (5, 1), (5, 0), (6, 1), (7, 0), (7, 1), (6, 2)])
    puzzle.add_palindrome([(2, 3), (3, 2), (2, 1), (1, 1), (0, 0)])
    puzzle.add_palindrome([(2, 5), (2, 4), (1, 3), (0, 2), (1, 2), (0, 1)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 7), (6, 8)])
    puzzle.add_palindrome([(7, 2), (6, 3), (5, 4), (4, 4)])

    return puzzle
