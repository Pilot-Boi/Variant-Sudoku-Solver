"""PuzzleMadness Palindrome Sudoku — 2025-11-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 9, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 3, 0],
        [0, 2, 0, 0, 0, 0, 3, 0, 0],
        [6, 0, 0, 0, 0, 7, 2, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 4, 6, 0, 5, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (3, 2), (3, 1), (2, 0), (1, 0), (0, 0), (0, 1)])
    puzzle.add_palindrome([(4, 4), (5, 5), (4, 6), (3, 6), (2, 5)])
    puzzle.add_palindrome([(8, 4), (7, 3), (6, 2), (6, 1), (6, 0)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 3), (4, 3)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 3)])
    puzzle.add_palindrome([(5, 6), (6, 7), (5, 8), (6, 8)])

    return puzzle
