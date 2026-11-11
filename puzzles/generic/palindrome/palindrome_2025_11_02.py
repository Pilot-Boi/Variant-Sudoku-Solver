"""PuzzleMadness Palindrome Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 3, 0],
        [9, 0, 7, 0, 0, 0, 0, 0, 1],
        [0, 0, 6, 0, 0, 0, 0, 9, 4],
        [0, 0, 3, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 4), (5, 3), (5, 2), (6, 2), (7, 1), (6, 1)])
    puzzle.add_palindrome([(8, 7), (7, 6), (6, 6), (7, 5), (6, 5), (5, 6)])
    puzzle.add_palindrome([(4, 1), (3, 1), (3, 0), (2, 0), (1, 0)])
    puzzle.add_palindrome([(2, 4), (2, 5), (1, 6), (0, 7)])
    puzzle.add_palindrome([(0, 2), (0, 3), (1, 2), (2, 3)])
    puzzle.add_palindrome([(1, 7), (2, 7), (3, 8)])

    return puzzle
