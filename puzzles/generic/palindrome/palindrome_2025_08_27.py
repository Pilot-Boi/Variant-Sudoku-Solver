"""PuzzleMadness Palindrome Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 3, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 1, 8],
        [0, 1, 0, 9, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 5), (2, 4), (2, 3), (1, 2), (0, 1), (1, 0), (0, 0)])
    puzzle.add_palindrome([(4, 2), (4, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_palindrome([(5, 6), (4, 6), (3, 6), (3, 5), (4, 5)])
    puzzle.add_palindrome([(2, 1), (3, 1), (3, 2)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (1, 4)])
    puzzle.add_palindrome([(7, 4), (7, 5), (8, 6), (8, 7)])

    return puzzle
