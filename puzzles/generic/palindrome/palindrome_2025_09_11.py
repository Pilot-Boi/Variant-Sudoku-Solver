"""PuzzleMadness Palindrome Sudoku — 2025-09-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [2, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 8, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 2, 5, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 7), (5, 7), (4, 7), (4, 6), (3, 5), (4, 4), (3, 4)])
    puzzle.add_palindrome([(1, 3), (0, 2), (1, 2), (2, 3), (3, 3), (4, 2)])
    puzzle.add_palindrome([(7, 0), (7, 1), (6, 2), (5, 2), (5, 1)])
    puzzle.add_palindrome([(8, 6), (7, 6), (8, 5), (7, 4)])
    puzzle.add_palindrome([(4, 1), (5, 0), (6, 0)])

    return puzzle
