"""PuzzleMadness Palindrome Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 5, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 9, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 2), (1, 3), (0, 4), (0, 3), (1, 2), (1, 1), (2, 0), (3, 0)])
    puzzle.add_palindrome([(4, 4), (4, 5), (3, 4), (2, 3), (3, 2), (3, 1)])
    puzzle.add_palindrome([(5, 3), (5, 2), (5, 1), (6, 0), (6, 1)])
    puzzle.add_palindrome([(4, 6), (4, 7), (3, 6), (2, 7), (2, 8), (1, 7)])
    puzzle.add_palindrome([(6, 4), (7, 3), (8, 2)])
    puzzle.add_palindrome([(6, 7), (7, 6), (8, 5)])

    return puzzle
