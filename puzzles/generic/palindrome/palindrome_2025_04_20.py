"""PuzzleMadness Palindrome Sudoku — 2025-04-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 8, 0],
        [0, 0, 6, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 4, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 7), (4, 8), (5, 7), (5, 8), (6, 7), (7, 6), (8, 7), (7, 8)])
    puzzle.add_palindrome([(4, 6), (3, 5), (2, 4), (1, 4), (1, 3)])
    puzzle.add_palindrome([(4, 3), (4, 4), (3, 3), (2, 2), (3, 1)])
    puzzle.add_palindrome([(2, 1), (2, 0), (3, 0)])
    puzzle.add_palindrome([(6, 5), (6, 4), (5, 3), (5, 4)])
    puzzle.add_palindrome([(5, 1), (5, 2), (6, 3), (7, 3)])

    return puzzle
