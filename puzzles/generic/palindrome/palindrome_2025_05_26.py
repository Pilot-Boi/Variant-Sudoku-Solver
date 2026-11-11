"""PuzzleMadness Palindrome Sudoku — 2025-05-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 5, 6, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 1, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 5, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 1), (2, 2), (1, 1), (0, 2), (1, 3), (2, 3), (3, 3), (3, 2)])
    puzzle.add_palindrome([(0, 8), (1, 7), (0, 6), (1, 5), (2, 4), (1, 4)])
    puzzle.add_palindrome([(5, 4), (6, 3), (6, 4), (5, 5), (4, 6)])
    puzzle.add_palindrome([(6, 6), (5, 6), (6, 5), (7, 5)])
    puzzle.add_palindrome([(4, 4), (4, 5), (3, 6), (3, 7)])

    return puzzle
