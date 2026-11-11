"""PuzzleMadness Palindrome Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 6, 0, 0, 3, 0],
        [0, 0, 0, 0, 2, 5, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (0, 7), (1, 8), (2, 7), (3, 7), (4, 6), (4, 7)])
    puzzle.add_palindrome([(2, 0), (1, 0), (2, 1), (3, 0), (4, 1), (5, 2)])
    puzzle.add_palindrome([(7, 1), (6, 0), (6, 1), (5, 1), (5, 0)])
    puzzle.add_palindrome([(4, 2), (4, 3), (3, 3)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 3), (2, 4)])

    return puzzle
