"""PuzzleMadness Palindrome Sudoku — 2025-06-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 1, 0, 9, 0, 6, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 3],
        [0, 0, 4, 3, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 6), (1, 6), (2, 7), (3, 7), (2, 8), (3, 8), (4, 8), (5, 8)])
    puzzle.add_palindrome([(1, 2), (1, 1), (2, 2), (3, 1), (3, 2), (2, 3)])
    puzzle.add_palindrome([(6, 4), (6, 3), (5, 2), (5, 1), (4, 2)])
    puzzle.add_palindrome([(4, 7), (4, 6), (3, 5), (2, 5)])
    puzzle.add_palindrome([(7, 7), (6, 6), (5, 6)])

    return puzzle
