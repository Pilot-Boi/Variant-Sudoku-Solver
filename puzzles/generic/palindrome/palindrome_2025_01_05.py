"""PuzzleMadness Palindrome Sudoku — 2025-01-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 7, 6, 9, 4, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 0, 0, 8, 0, 2],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 6), (3, 7), (2, 7), (1, 6), (1, 5), (1, 4), (0, 4)])
    puzzle.add_palindrome([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)])
    puzzle.add_palindrome([(5, 1), (4, 1), (3, 2), (2, 1), (2, 0), (1, 0)])
    puzzle.add_palindrome([(8, 5), (7, 5), (6, 6)])
    puzzle.add_palindrome([(7, 1), (6, 1), (5, 2)])
    puzzle.add_palindrome([(5, 4), (4, 5), (4, 6)])

    return puzzle
