"""PuzzleMadness Palindrome Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [8, 0, 2, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 4, 0, 5, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 2, 0, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 3), (4, 2), (4, 1), (5, 2), (6, 1), (7, 0), (8, 0), (8, 1)])
    puzzle.add_palindrome([(3, 7), (4, 8), (3, 8), (2, 7), (2, 6)])
    puzzle.add_palindrome([(8, 7), (7, 6), (6, 6), (5, 5), (6, 4), (7, 3)])
    puzzle.add_palindrome([(0, 0), (0, 1), (1, 2), (2, 3), (2, 4), (1, 3)])
    puzzle.add_palindrome([(2, 2), (3, 3), (3, 4)])
    puzzle.add_palindrome([(8, 2), (8, 3), (7, 4)])

    return puzzle
