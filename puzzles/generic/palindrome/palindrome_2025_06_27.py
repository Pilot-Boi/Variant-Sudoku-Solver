"""PuzzleMadness Palindrome Sudoku — 2025-06-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 9, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 4, 0, 0, 0, 1],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (7, 2), (6, 3), (6, 4), (5, 4), (5, 3), (4, 3)])
    puzzle.add_palindrome([(6, 7), (7, 7), (8, 6), (7, 5), (6, 5), (5, 5)])
    puzzle.add_palindrome([(2, 3), (1, 3), (0, 3), (1, 2), (2, 2), (3, 1)])
    puzzle.add_palindrome([(4, 2), (3, 3), (2, 4), (3, 5), (4, 6), (3, 7)])
    puzzle.add_palindrome([(2, 6), (3, 6), (2, 7), (3, 8)])
    puzzle.add_palindrome([(4, 7), (5, 7), (6, 6)])

    return puzzle
