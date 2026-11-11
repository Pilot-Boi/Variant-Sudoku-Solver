"""PuzzleMadness Palindrome Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 8, 0, 0, 0, 0, 9, 0, 3],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 8, 0, 9],
        [0, 0, 0, 7, 6, 9, 0, 2, 0],
        [0, 0, 0, 0, 5, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (3, 4), (3, 3), (3, 2), (2, 1), (2, 2), (1, 1)])
    puzzle.add_palindrome([(4, 1), (3, 1), (4, 2), (4, 3), (5, 4)])
    puzzle.add_palindrome([(1, 3), (2, 4), (2, 5), (1, 6), (0, 6)])
    puzzle.add_palindrome([(7, 7), (6, 8), (5, 8)])
    puzzle.add_palindrome([(4, 7), (3, 7), (2, 8), (1, 8)])

    return puzzle
