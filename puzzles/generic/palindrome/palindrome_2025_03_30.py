"""PuzzleMadness Palindrome Sudoku — 2025-03-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 2],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 5, 0],
        [7, 0, 9, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (6, 2), (7, 3), (6, 3), (5, 4), (4, 5), (4, 6)])
    puzzle.add_palindrome([(2, 4), (3, 4), (3, 3), (4, 2), (5, 1), (4, 1)])
    puzzle.add_palindrome([(2, 3), (1, 3), (1, 2), (0, 1), (1, 1)])
    puzzle.add_palindrome([(6, 7), (5, 8), (4, 8)])
    puzzle.add_palindrome([(2, 5), (3, 6), (2, 7), (1, 8)])
    puzzle.add_palindrome([(2, 8), (3, 8), (4, 7)])

    return puzzle
