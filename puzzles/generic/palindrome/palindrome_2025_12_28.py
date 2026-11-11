"""PuzzleMadness Palindrome Sudoku — 2025-12-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 7],
        [1, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 1],
        [9, 2, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 4), (0, 4), (0, 5), (1, 5), (0, 6), (1, 7), (2, 7), (2, 8)])
    puzzle.add_palindrome([(3, 6), (2, 6), (3, 5), (4, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(7, 6), (6, 7), (6, 8), (5, 7), (4, 8), (4, 7)])
    puzzle.add_palindrome([(4, 2), (3, 1), (2, 0), (2, 1)])
    puzzle.add_palindrome([(4, 3), (5, 3), (6, 4), (7, 4)])

    return puzzle
