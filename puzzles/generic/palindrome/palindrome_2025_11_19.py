"""PuzzleMadness Palindrome Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [4, 8, 0, 0, 3, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 2), (5, 3), (4, 2), (3, 3), (2, 2), (1, 1), (0, 0), (0, 1)])
    puzzle.add_palindrome([(4, 6), (4, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_palindrome([(6, 7), (7, 6), (6, 6), (5, 7), (4, 8), (5, 8)])
    puzzle.add_palindrome([(3, 7), (3, 6), (2, 7), (1, 6)])
    puzzle.add_palindrome([(2, 4), (3, 4), (3, 5)])
    puzzle.add_palindrome([(7, 3), (7, 2), (6, 1)])

    return puzzle
