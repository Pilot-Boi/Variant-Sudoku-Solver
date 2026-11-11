"""PuzzleMadness Palindrome Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 8, 4],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 1, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 4, 0, 3],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 6), (7, 5), (6, 5), (6, 4), (5, 3), (4, 3), (3, 3), (3, 4)])
    puzzle.add_palindrome([(1, 3), (0, 4), (0, 3), (1, 2), (1, 1), (2, 0)])
    puzzle.add_palindrome([(6, 1), (7, 1), (6, 0), (5, 1), (5, 2), (4, 2)])
    puzzle.add_palindrome([(6, 8), (6, 7), (5, 6), (5, 7)])
    puzzle.add_palindrome([(7, 3), (8, 3), (7, 2), (8, 1)])

    return puzzle
