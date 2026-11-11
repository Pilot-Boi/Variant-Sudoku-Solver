"""PuzzleMadness Palindrome Sudoku — 2025-10-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 3, 6, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 7, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 1, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 7), (7, 8), (6, 8), (6, 7), (5, 6), (4, 6), (5, 5), (4, 4)])
    puzzle.add_palindrome([(5, 0), (4, 1), (4, 2), (3, 3), (2, 2), (2, 1)])
    puzzle.add_palindrome([(5, 4), (6, 3), (5, 2), (6, 1), (7, 0), (8, 0)])
    puzzle.add_palindrome([(1, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(6, 5), (7, 6), (8, 6)])
    puzzle.add_palindrome([(1, 2), (2, 3), (3, 4), (2, 5)])

    return puzzle
