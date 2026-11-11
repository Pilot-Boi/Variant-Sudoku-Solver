"""PuzzleMadness Palindrome Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 5, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 8, 6, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 4), (7, 4), (8, 3), (7, 2), (8, 2), (7, 1), (7, 0)])
    puzzle.add_palindrome([(1, 5), (1, 4), (2, 4), (3, 5), (4, 6), (5, 7)])
    puzzle.add_palindrome([(6, 0), (6, 1), (6, 2), (5, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(6, 5), (7, 6), (7, 7)])
    puzzle.add_palindrome([(4, 3), (3, 3), (2, 2), (1, 1)])

    return puzzle
