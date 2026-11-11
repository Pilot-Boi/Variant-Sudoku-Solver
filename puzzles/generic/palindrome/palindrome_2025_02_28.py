"""PuzzleMadness Palindrome Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 9, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 7],
        [0, 7, 0, 2, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 3), (2, 2), (3, 1), (3, 2), (4, 3), (4, 4), (3, 4), (4, 5)])
    puzzle.add_palindrome([(1, 7), (1, 6), (2, 5), (3, 5), (3, 6)])
    puzzle.add_palindrome([(7, 6), (7, 7), (6, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_palindrome([(6, 6), (5, 5), (4, 6), (3, 7)])
    puzzle.add_palindrome([(7, 4), (6, 3), (7, 2), (6, 1)])
    puzzle.add_palindrome([(8, 3), (8, 2), (7, 1)])

    return puzzle
