"""PuzzleMadness Palindrome Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 2, 0, 7, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [9, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 1), (4, 1), (5, 2), (4, 3), (3, 3), (3, 4), (2, 4)])
    puzzle.add_palindrome([(0, 2), (1, 2), (2, 2), (3, 1), (4, 0)])
    puzzle.add_palindrome([(7, 5), (7, 6), (6, 7), (5, 8), (4, 7), (4, 6)])
    puzzle.add_palindrome([(4, 5), (3, 6), (2, 6), (1, 5), (2, 5), (1, 4)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 8), (3, 7)])
    puzzle.add_palindrome([(8, 1), (7, 2), (6, 3)])
    puzzle.add_palindrome([(5, 4), (5, 5), (6, 6), (6, 5)])

    return puzzle
