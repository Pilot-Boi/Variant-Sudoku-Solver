"""PuzzleMadness Palindrome Sudoku — 2025-01-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 4],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 8, 0],
        [0, 0, 5, 0, 6, 0, 0, 0, 0],
        [0, 9, 0, 4, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 6), (4, 6), (3, 7), (3, 6), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_palindrome([(4, 3), (5, 4), (5, 5), (6, 5), (7, 5)])
    puzzle.add_palindrome([(4, 1), (3, 1), (3, 0), (2, 1), (2, 0), (1, 0)])
    puzzle.add_palindrome([(5, 7), (6, 7), (7, 6)])
    puzzle.add_palindrome([(6, 2), (6, 3), (7, 3)])
    puzzle.add_palindrome([(2, 5), (1, 6), (0, 6)])

    return puzzle
