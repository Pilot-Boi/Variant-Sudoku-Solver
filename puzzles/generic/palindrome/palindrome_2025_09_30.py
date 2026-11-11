"""PuzzleMadness Palindrome Sudoku — 2025-09-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 1, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 7],
        [0, 3, 0, 0, 2, 0, 0, 0, 0],
        [6, 0, 0, 8, 0, 4, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
        [0, 9, 0, 1, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (2, 5), (1, 5), (1, 6), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_palindrome([(7, 1), (8, 2), (7, 3), (6, 3), (6, 4)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 2), (1, 3), (0, 3)])
    puzzle.add_palindrome([(2, 6), (2, 7), (3, 8), (4, 8)])
    puzzle.add_palindrome([(8, 5), (7, 5), (7, 6)])

    return puzzle
