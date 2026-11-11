"""PuzzleMadness Palindrome Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 4, 0, 0, 0],
        [9, 2, 0, 0, 8, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [5, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (4, 3), (3, 3), (2, 2), (1, 3), (1, 4), (0, 4), (0, 5)])
    puzzle.add_palindrome([(2, 6), (1, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_palindrome([(4, 1), (3, 0), (3, 1), (2, 0), (1, 1), (1, 2)])
    puzzle.add_palindrome([(5, 1), (4, 2), (5, 2), (6, 1), (6, 0)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 3), (7, 3)])
    puzzle.add_palindrome([(5, 6), (6, 7), (6, 8)])

    return puzzle
