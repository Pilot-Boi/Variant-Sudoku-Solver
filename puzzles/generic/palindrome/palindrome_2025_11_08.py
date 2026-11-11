"""PuzzleMadness Palindrome Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 8, 0, 0, 7, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 3, 0, 0, 0, 0, 5, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 2), (7, 2), (7, 1), (8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(4, 3), (3, 2), (3, 1), (2, 0), (1, 0), (0, 1)])
    puzzle.add_palindrome([(5, 7), (4, 8), (5, 8), (6, 7), (7, 6), (8, 6)])
    puzzle.add_palindrome([(2, 7), (3, 7), (2, 6), (1, 5), (0, 4), (0, 5)])
    puzzle.add_palindrome([(5, 2), (5, 1), (6, 0), (6, 1)])
    puzzle.add_palindrome([(2, 1), (1, 2), (1, 3)])

    return puzzle
