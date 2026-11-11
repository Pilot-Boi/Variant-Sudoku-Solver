"""PuzzleMadness Palindrome Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 9, 6, 0, 0],
        [0, 4, 0, 0, 0, 0, 2, 0, 0],
        [0, 6, 0, 0, 8, 3, 0, 0, 9],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (1, 4), (1, 5), (2, 5), (1, 6), (0, 7), (0, 8), (1, 7)])
    puzzle.add_palindrome([(5, 4), (6, 3), (5, 3), (6, 2), (7, 1), (7, 2)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 0), (6, 1), (5, 1), (5, 2)])
    puzzle.add_palindrome([(5, 6), (5, 5), (6, 5)])
    puzzle.add_palindrome([(1, 1), (2, 0), (3, 0)])

    return puzzle
