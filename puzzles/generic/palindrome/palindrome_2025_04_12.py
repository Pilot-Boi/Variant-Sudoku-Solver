"""PuzzleMadness Palindrome Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 8, 4, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 8, 1, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2), (2, 2), (3, 1), (4, 1), (4, 2), (3, 3)])
    puzzle.add_palindrome([(7, 6), (6, 6), (5, 5), (6, 4), (7, 3), (8, 4)])
    puzzle.add_palindrome([(2, 5), (3, 5), (4, 5), (5, 6), (5, 7)])
    puzzle.add_palindrome([(5, 0), (6, 1), (7, 2)])
    puzzle.add_palindrome([(1, 6), (2, 6), (3, 7)])

    return puzzle
