"""PuzzleMadness Palindrome Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 9, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 9],
        [3, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 6, 0, 5, 0, 2, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 8), (1, 7), (1, 6), (2, 5), (3, 4), (3, 3), (2, 3), (1, 4)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2), (1, 1), (1, 0)])
    puzzle.add_palindrome([(2, 1), (2, 0), (3, 1), (4, 1), (4, 2)])
    puzzle.add_palindrome([(8, 2), (7, 3), (7, 4)])
    puzzle.add_palindrome([(5, 0), (6, 1), (7, 1)])
    puzzle.add_palindrome([(2, 8), (2, 7), (3, 7)])

    return puzzle
