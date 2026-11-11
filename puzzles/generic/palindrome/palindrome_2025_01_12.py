"""PuzzleMadness Palindrome Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 7, 6, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [4, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (0, 0), (1, 0), (2, 1), (3, 2), (4, 2), (4, 3), (5, 4)])
    puzzle.add_palindrome([(6, 1), (7, 1), (6, 0), (5, 1), (5, 2), (5, 3)])
    puzzle.add_palindrome([(5, 7), (4, 7), (3, 7), (2, 6), (3, 5), (3, 4)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (2, 5)])
    puzzle.add_palindrome([(5, 5), (4, 5), (4, 6)])
    puzzle.add_palindrome([(8, 5), (7, 6), (7, 7)])

    return puzzle
