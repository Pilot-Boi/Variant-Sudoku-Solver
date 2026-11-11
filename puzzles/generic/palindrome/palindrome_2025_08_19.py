"""PuzzleMadness Palindrome Sudoku — 2025-08-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 0, 0, 0, 0, 0],
        [0, 8, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 6, 0, 0],
        [3, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 4), (8, 5), (7, 4), (6, 5), (7, 6), (8, 6), (7, 7), (6, 8)])
    puzzle.add_palindrome([(5, 1), (6, 1), (6, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 2), (2, 3), (1, 4)])
    puzzle.add_palindrome([(3, 6), (2, 5), (3, 4), (2, 4)])
    puzzle.add_palindrome([(6, 7), (5, 7), (4, 6)])

    return puzzle
