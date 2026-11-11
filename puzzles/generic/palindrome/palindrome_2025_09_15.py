"""PuzzleMadness Palindrome Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 8],
        [1, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 5, 0, 0],
        [3, 0, 0, 0, 4, 0, 7, 0, 0],
        [0, 0, 0, 7, 5, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 0), (4, 1), (4, 0), (5, 1), (6, 2), (6, 1), (7, 2), (8, 2)])
    puzzle.add_palindrome([(2, 6), (2, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_palindrome([(2, 0), (1, 1), (2, 2), (3, 2), (4, 3)])
    puzzle.add_palindrome([(2, 3), (1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(2, 5), (1, 6), (0, 5), (0, 6)])
    puzzle.add_palindrome([(8, 6), (7, 6), (6, 5), (5, 5)])

    return puzzle
