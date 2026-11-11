"""PuzzleMadness Palindrome Sudoku — 2025-01-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 5],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 4, 0, 8, 0, 0, 0, 2],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (5, 3), (4, 2), (5, 1), (6, 0), (7, 1), (7, 2), (8, 1)])
    puzzle.add_palindrome([(2, 3), (1, 4), (1, 3), (0, 2), (0, 1), (1, 2)])
    puzzle.add_palindrome([(5, 5), (4, 6), (3, 6), (4, 5), (5, 4), (6, 3)])
    puzzle.add_palindrome([(3, 1), (3, 0), (2, 1), (1, 1), (2, 0)])
    puzzle.add_palindrome([(3, 8), (2, 7), (1, 6)])
    puzzle.add_palindrome([(2, 2), (3, 2), (4, 3), (4, 4)])
    puzzle.add_palindrome([(1, 7), (0, 6), (1, 5), (0, 5)])

    return puzzle
