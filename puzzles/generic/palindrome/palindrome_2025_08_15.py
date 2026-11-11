"""PuzzleMadness Palindrome Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [7, 0, 3, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 9, 0, 4],
        [0, 0, 0, 1, 8, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 8), (3, 8), (4, 7), (3, 7), (2, 8), (1, 7), (1, 6)])
    puzzle.add_palindrome([(7, 7), (7, 6), (6, 5), (5, 5), (5, 4)])
    puzzle.add_palindrome([(4, 0), (5, 0), (6, 1), (7, 2), (6, 2)])
    puzzle.add_palindrome([(4, 4), (4, 3), (3, 2), (2, 3), (1, 4), (2, 5)])
    puzzle.add_palindrome([(0, 2), (1, 2), (1, 3)])
    puzzle.add_palindrome([(6, 7), (6, 8), (5, 7), (5, 8)])

    return puzzle
