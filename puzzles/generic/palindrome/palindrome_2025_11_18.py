"""PuzzleMadness Palindrome Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 6, 0, 0],
        [0, 0, 0, 8, 3, 0, 0, 0, 0],
        [0, 0, 2, 9, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 4), (3, 3), (4, 3), (5, 4), (6, 3), (7, 2), (6, 2), (5, 2)])
    puzzle.add_palindrome([(1, 2), (2, 2), (2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(2, 7), (1, 6), (1, 5), (2, 6), (3, 7), (4, 6)])
    puzzle.add_palindrome([(0, 1), (0, 2), (1, 3)])
    puzzle.add_palindrome([(7, 4), (6, 5), (7, 6), (6, 6)])
    puzzle.add_palindrome([(5, 6), (6, 7), (7, 7)])

    return puzzle
