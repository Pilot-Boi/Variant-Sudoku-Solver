"""PuzzleMadness Palindrome Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 1, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 7, 0, 4],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 5, 0, 1, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (5, 3), (5, 2), (6, 2), (7, 1), (8, 0), (7, 0)])
    puzzle.add_palindrome([(3, 2), (2, 3), (1, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(5, 4), (6, 5), (5, 6), (6, 7), (7, 8), (8, 8)])
    puzzle.add_palindrome([(0, 5), (1, 6), (2, 6)])
    puzzle.add_palindrome([(8, 2), (7, 2), (6, 3), (7, 3)])

    return puzzle
