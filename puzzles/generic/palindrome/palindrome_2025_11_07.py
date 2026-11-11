"""PuzzleMadness Palindrome Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 1, 0, 6, 0],
        [5, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 1, 8],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (1, 6), (2, 6), (2, 7), (3, 6), (3, 7), (4, 8), (5, 8)])
    puzzle.add_palindrome([(4, 4), (3, 5), (3, 4), (2, 4), (2, 5)])
    puzzle.add_palindrome([(5, 3), (6, 2), (5, 1), (5, 0), (6, 1)])
    puzzle.add_palindrome([(7, 1), (8, 2), (7, 2), (6, 3), (5, 4)])
    puzzle.add_palindrome([(0, 1), (1, 2), (0, 3), (1, 3)])
    puzzle.add_palindrome([(5, 6), (6, 7), (7, 8)])
    puzzle.add_palindrome([(4, 2), (3, 3), (2, 2), (1, 1)])

    return puzzle
