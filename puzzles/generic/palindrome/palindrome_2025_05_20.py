"""PuzzleMadness Palindrome Sudoku — 2025-05-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 3, 8, 7, 0, 0, 1, 6],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 6), (6, 5), (5, 5), (4, 6), (3, 5), (2, 6), (1, 7), (0, 7)])
    puzzle.add_palindrome([(6, 7), (6, 6), (5, 6), (4, 7), (4, 8)])
    puzzle.add_palindrome([(7, 3), (7, 4), (6, 3), (7, 2), (6, 1), (6, 0)])
    puzzle.add_palindrome([(0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(2, 2), (3, 3), (4, 4)])
    puzzle.add_palindrome([(1, 8), (2, 8), (3, 7)])

    return puzzle
