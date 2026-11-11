"""PuzzleMadness Palindrome Sudoku — 2025-01-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 0, 0, 9, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [1, 0, 4, 2, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (5, 7), (6, 6), (7, 6), (7, 5), (8, 6), (7, 7)])
    puzzle.add_palindrome([(3, 0), (4, 0), (3, 1), (2, 2), (1, 1), (0, 1)])
    puzzle.add_palindrome([(8, 5), (7, 4), (6, 3), (5, 2), (6, 1)])
    puzzle.add_palindrome([(3, 6), (3, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_palindrome([(4, 5), (5, 6), (6, 5), (6, 4)])
    puzzle.add_palindrome([(0, 6), (0, 5), (1, 5)])
    puzzle.add_palindrome([(4, 2), (3, 3), (3, 4)])

    return puzzle
