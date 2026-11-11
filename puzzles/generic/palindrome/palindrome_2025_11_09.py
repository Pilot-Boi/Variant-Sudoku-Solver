"""PuzzleMadness Palindrome Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 6],
        [0, 9, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 1), (8, 0), (7, 1), (8, 2), (7, 3), (6, 4), (6, 3), (5, 4)])
    puzzle.add_palindrome([(2, 1), (3, 1), (2, 2), (2, 3), (3, 3)])
    puzzle.add_palindrome([(1, 8), (0, 7), (1, 6), (1, 5), (2, 5)])
    puzzle.add_palindrome([(2, 4), (1, 3), (1, 2)])
    puzzle.add_palindrome([(6, 0), (6, 1), (5, 2)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 7)])

    return puzzle
