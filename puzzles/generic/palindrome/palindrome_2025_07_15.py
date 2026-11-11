"""PuzzleMadness Palindrome Sudoku — 2025-07-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 8, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 7],
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 3, 2, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (1, 4), (2, 5), (1, 6), (1, 7), (0, 7), (0, 8)])
    puzzle.add_palindrome([(5, 2), (4, 1), (5, 0), (6, 1), (7, 0), (8, 1)])
    puzzle.add_palindrome([(2, 1), (1, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_palindrome([(7, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2)])
    puzzle.add_palindrome([(4, 4), (3, 5), (4, 6), (3, 7)])
    puzzle.add_palindrome([(1, 3), (0, 3), (0, 2)])

    return puzzle
