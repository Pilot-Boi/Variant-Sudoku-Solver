"""PuzzleMadness Palindrome Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 2, 0, 0, 4, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 2), (6, 1), (6, 2), (6, 3), (7, 4), (7, 5), (8, 5)])
    puzzle.add_palindrome([(2, 1), (1, 2), (0, 3), (0, 4), (1, 4)])
    puzzle.add_palindrome([(0, 7), (1, 7), (0, 6), (0, 5), (1, 5)])
    puzzle.add_palindrome([(6, 5), (7, 6), (6, 7), (5, 8), (5, 7)])
    puzzle.add_palindrome([(6, 4), (5, 3), (4, 3)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(2, 5), (3, 6), (2, 7), (1, 6)])

    return puzzle
