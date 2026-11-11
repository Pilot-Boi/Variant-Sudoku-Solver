"""PuzzleMadness Palindrome Sudoku — 2025-07-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 7],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 2, 0],
        [0, 0, 0, 0, 4, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 3, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (6, 3), (6, 4), (5, 5), (6, 6), (5, 6), (4, 5), (4, 6)])
    puzzle.add_palindrome([(3, 4), (3, 5), (2, 5), (1, 6), (2, 6)])
    puzzle.add_palindrome([(3, 3), (4, 2), (3, 1), (2, 0), (1, 1), (1, 0)])
    puzzle.add_palindrome([(6, 1), (6, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(2, 4), (1, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(0, 5), (1, 5), (0, 6), (1, 7)])

    return puzzle
