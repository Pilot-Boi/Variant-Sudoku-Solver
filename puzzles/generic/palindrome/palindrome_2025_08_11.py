"""PuzzleMadness Palindrome Sudoku — 2025-08-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 7, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 1, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 6, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 7), (6, 6), (5, 6), (6, 5), (7, 5), (8, 4), (8, 3)])
    puzzle.add_palindrome([(8, 2), (7, 2), (6, 1), (5, 1), (5, 0)])
    puzzle.add_palindrome([(3, 7), (3, 8), (2, 8), (1, 7), (1, 8)])
    puzzle.add_palindrome([(4, 4), (3, 3), (3, 4), (2, 5), (3, 6)])
    puzzle.add_palindrome([(4, 3), (5, 2), (6, 2)])
    puzzle.add_palindrome([(5, 5), (4, 5), (4, 6)])
    puzzle.add_palindrome([(4, 7), (5, 8), (6, 7), (7, 8)])

    return puzzle
