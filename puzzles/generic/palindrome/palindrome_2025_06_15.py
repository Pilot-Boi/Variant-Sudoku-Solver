"""PuzzleMadness Palindrome Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 5, 0, 0, 1, 0],
        [0, 0, 8, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (0, 0), (1, 1), (2, 0), (3, 1), (3, 2), (4, 2), (5, 2)])
    puzzle.add_palindrome([(8, 2), (7, 2), (6, 2), (5, 3), (4, 4)])
    puzzle.add_palindrome([(5, 6), (4, 7), (3, 7), (2, 6), (1, 7)])
    puzzle.add_palindrome([(4, 5), (3, 5), (3, 4), (2, 3), (2, 2), (1, 3)])
    puzzle.add_palindrome([(8, 7), (8, 6), (7, 5), (6, 4)])
    puzzle.add_palindrome([(5, 8), (6, 8), (6, 7)])
    puzzle.add_palindrome([(4, 8), (5, 7), (6, 6)])

    return puzzle
