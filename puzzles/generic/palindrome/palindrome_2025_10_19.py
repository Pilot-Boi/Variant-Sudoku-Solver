"""PuzzleMadness Palindrome Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 7],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 2, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 3, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 1, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (7, 4), (6, 4), (5, 5), (4, 6), (3, 6), (4, 7), (5, 6)])
    puzzle.add_palindrome([(7, 7), (6, 7), (7, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_palindrome([(0, 6), (0, 7), (1, 6), (0, 5), (1, 4), (2, 4)])
    puzzle.add_palindrome([(2, 3), (3, 2), (2, 1), (3, 0)])
    puzzle.add_palindrome([(4, 2), (5, 2), (6, 1)])

    return puzzle
