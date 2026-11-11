"""PuzzleMadness Palindrome Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 7, 0, 5, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 4, 9, 0, 3],
        [0, 0, 4, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (4, 5), (3, 4), (2, 5), (1, 6), (0, 7), (1, 8), (1, 7)])
    puzzle.add_palindrome([(7, 1), (6, 1), (5, 1), (6, 2), (7, 3), (8, 3)])
    puzzle.add_palindrome([(3, 1), (2, 2), (1, 3), (0, 3), (0, 2)])
    puzzle.add_palindrome([(5, 3), (5, 2), (6, 3), (6, 4)])
    puzzle.add_palindrome([(1, 4), (0, 5), (0, 6)])

    return puzzle
