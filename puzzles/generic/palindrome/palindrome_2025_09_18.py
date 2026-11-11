"""PuzzleMadness Palindrome Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 1, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 0, 0, 0, 7, 0, 9, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 1, 0, 0, 2, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (7, 4), (7, 5), (6, 6), (6, 7), (6, 8), (7, 7)])
    puzzle.add_palindrome([(7, 1), (6, 2), (5, 2), (4, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(0, 2), (0, 1), (1, 2), (2, 3), (3, 3), (2, 4)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1), (4, 1)])
    puzzle.add_palindrome([(2, 1), (3, 0), (4, 0)])

    return puzzle
