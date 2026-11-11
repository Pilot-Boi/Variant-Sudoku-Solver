"""PuzzleMadness Palindrome Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 5, 0, 0],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 2, 0, 0, 0, 4],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 4), (3, 5), (3, 6), (2, 6), (3, 7), (4, 7)])
    puzzle.add_palindrome([(4, 8), (5, 8), (6, 8), (5, 7), (6, 7), (7, 6)])
    puzzle.add_palindrome([(1, 6), (1, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(7, 2), (6, 2), (5, 3), (6, 4)])
    puzzle.add_palindrome([(4, 1), (4, 2), (3, 3), (3, 4)])

    return puzzle
