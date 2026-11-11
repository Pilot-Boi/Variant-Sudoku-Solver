"""PuzzleMadness Palindrome Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 9, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 7, 9, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (4, 3), (5, 3), (4, 2), (3, 2), (2, 2), (1, 3)])
    puzzle.add_palindrome([(7, 7), (6, 8), (5, 8), (4, 7), (4, 6)])
    puzzle.add_palindrome([(2, 7), (1, 7), (2, 8), (3, 7), (3, 8), (4, 8)])
    puzzle.add_palindrome([(8, 0), (7, 0), (6, 1), (5, 1), (5, 2)])
    puzzle.add_palindrome([(4, 5), (5, 4), (6, 3), (6, 2)])
    puzzle.add_palindrome([(1, 1), (1, 2), (0, 3)])

    return puzzle
