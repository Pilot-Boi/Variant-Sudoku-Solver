"""PuzzleMadness Palindrome Sudoku — 2025-02-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 4, 2, 0, 0, 8],
        [4, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 7, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (8, 5), (7, 6), (7, 5), (6, 6), (5, 7), (6, 8), (5, 8)])
    puzzle.add_palindrome([(2, 6), (3, 7), (4, 6), (5, 5), (6, 4), (6, 5)])
    puzzle.add_palindrome([(7, 2), (6, 3), (5, 4), (4, 5), (3, 6)])
    puzzle.add_palindrome([(0, 2), (0, 3), (1, 3)])
    puzzle.add_palindrome([(4, 1), (3, 0), (2, 1), (2, 2)])

    return puzzle
