"""PuzzleMadness Palindrome Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 1, 3, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 3), (4, 4), (5, 3), (6, 4), (6, 5), (7, 5), (8, 6)])
    puzzle.add_palindrome([(1, 0), (2, 1), (3, 2), (4, 3), (4, 2), (5, 2)])
    puzzle.add_palindrome([(8, 7), (7, 7), (6, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_palindrome([(4, 6), (3, 5), (3, 4), (2, 5), (2, 6), (1, 7)])
    puzzle.add_palindrome([(2, 2), (1, 3), (0, 4)])
    puzzle.add_palindrome([(8, 3), (7, 2), (6, 1)])

    return puzzle
