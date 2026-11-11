"""PuzzleMadness Palindrome Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 7, 0],
        [0, 8, 0, 2, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 3, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 8, 4, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 2), (4, 2), (4, 3), (3, 2), (2, 1), (1, 1), (2, 0)])
    puzzle.add_palindrome([(2, 2), (1, 2), (0, 2), (1, 3), (2, 4), (1, 4)])
    puzzle.add_palindrome([(3, 6), (4, 5), (5, 5), (6, 4), (7, 3), (6, 3)])
    puzzle.add_palindrome([(7, 7), (6, 8), (5, 8)])
    puzzle.add_palindrome([(2, 5), (2, 6), (3, 5), (3, 4)])

    return puzzle
