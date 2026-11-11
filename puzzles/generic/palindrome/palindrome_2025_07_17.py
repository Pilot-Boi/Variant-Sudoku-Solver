"""PuzzleMadness Palindrome Sudoku — 2025-07-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 7, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 4, 0, 0, 8, 0],
        [2, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 1, 0, 2, 0, 0, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 2), (7, 3), (8, 4), (7, 5), (7, 6), (8, 6), (8, 7)])
    puzzle.add_palindrome([(4, 7), (4, 6), (3, 6), (4, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(4, 0), (3, 1), (2, 1), (2, 2), (1, 2)])
    puzzle.add_palindrome([(7, 0), (6, 1), (5, 2), (5, 1)])
    puzzle.add_palindrome([(2, 4), (2, 3), (3, 3)])

    return puzzle
