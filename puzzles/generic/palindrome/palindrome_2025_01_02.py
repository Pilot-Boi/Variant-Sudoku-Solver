"""PuzzleMadness Palindrome Sudoku — 2025-01-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 3, 0, 0],
        [9, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 5, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 8, 0, 0, 4, 0, 3, 2],
        [0, 4, 0, 2, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (3, 1), (4, 2), (5, 1), (6, 1), (6, 2), (7, 1)])
    puzzle.add_palindrome([(0, 3), (1, 3), (2, 4), (3, 5), (4, 5), (5, 4)])
    puzzle.add_palindrome([(2, 6), (2, 7), (3, 7), (2, 8), (3, 8), (4, 7)])
    puzzle.add_palindrome([(6, 3), (7, 3), (7, 2)])
    puzzle.add_palindrome([(0, 5), (0, 6), (1, 5), (1, 6)])

    return puzzle
