"""PuzzleMadness Palindrome Sudoku — 2025-10-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 7, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 2, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 3), (7, 2), (6, 2), (5, 3), (4, 2), (3, 1), (3, 0), (4, 1)])
    puzzle.add_palindrome([(5, 7), (4, 8), (3, 8), (2, 7), (1, 6), (1, 5)])
    puzzle.add_palindrome([(1, 2), (2, 3), (3, 2), (4, 3), (4, 4), (5, 5)])
    puzzle.add_palindrome([(4, 5), (3, 4), (2, 5), (2, 6)])
    puzzle.add_palindrome([(1, 4), (0, 5), (0, 6)])

    return puzzle
