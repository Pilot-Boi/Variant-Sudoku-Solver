"""PuzzleMadness Palindrome Sudoku — 2025-01-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 6, 7, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 2, 0],
        [0, 4, 5, 0, 1, 0, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 5), (1, 4), (0, 3), (1, 2), (1, 1), (0, 1), (0, 2)])
    puzzle.add_palindrome([(1, 6), (1, 7), (2, 8), (3, 7), (3, 8), (4, 7)])
    puzzle.add_palindrome([(4, 2), (3, 2), (4, 3), (4, 4), (5, 5)])
    puzzle.add_palindrome([(6, 5), (7, 6), (6, 7), (5, 8), (5, 7), (4, 8)])
    puzzle.add_palindrome([(7, 4), (8, 5), (8, 6)])
    puzzle.add_palindrome([(6, 4), (6, 3), (7, 2), (8, 1)])

    return puzzle
