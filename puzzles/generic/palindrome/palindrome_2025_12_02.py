"""PuzzleMadness Palindrome Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 3],
        [0, 5, 0, 0, 0, 0, 0, 0, 7],
        [0, 7, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 6), (7, 6), (7, 5), (6, 4), (5, 3), (4, 3), (5, 2), (4, 1)])
    puzzle.add_palindrome([(5, 5), (6, 5), (5, 6), (6, 7), (5, 8), (4, 7)])
    puzzle.add_palindrome([(2, 4), (1, 3), (1, 2), (2, 3), (2, 2), (3, 3)])
    puzzle.add_palindrome([(2, 6), (3, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(6, 2), (5, 1), (4, 0)])

    return puzzle
