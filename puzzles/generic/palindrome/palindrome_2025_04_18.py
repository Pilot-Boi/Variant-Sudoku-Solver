"""PuzzleMadness Palindrome Sudoku — 2025-04-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 3, 0, 0, 7, 6, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 7, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 8), (1, 7), (1, 6), (0, 6), (1, 5), (2, 5), (3, 6), (4, 7)])
    puzzle.add_palindrome([(4, 6), (5, 7), (6, 7), (7, 8), (8, 8)])
    puzzle.add_palindrome([(1, 2), (2, 1), (3, 1), (4, 0), (3, 0)])
    puzzle.add_palindrome([(4, 1), (5, 1), (6, 0)])
    puzzle.add_palindrome([(7, 3), (6, 4), (5, 4)])
    puzzle.add_palindrome([(6, 2), (5, 3), (4, 2), (3, 3)])

    return puzzle
