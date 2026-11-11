"""PuzzleMadness Palindrome Sudoku — 2025-11-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 4, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 8, 0, 6, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 0), (4, 1), (3, 2), (4, 2), (3, 3), (2, 4), (1, 4), (0, 3)])
    puzzle.add_palindrome([(4, 6), (4, 7), (5, 6), (6, 7), (6, 6), (6, 5)])
    puzzle.add_palindrome([(2, 8), (1, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(6, 2), (5, 1), (6, 0), (5, 0)])
    puzzle.add_palindrome([(1, 6), (2, 7), (3, 6), (4, 5)])
    puzzle.add_palindrome([(3, 4), (2, 5), (2, 6)])

    return puzzle
