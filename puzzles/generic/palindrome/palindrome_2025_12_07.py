"""PuzzleMadness Palindrome Sudoku — 2025-12-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 7, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 2, 0],
        [0, 0, 1, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 0), (2, 1), (3, 2), (4, 2), (5, 3), (4, 3), (4, 4), (3, 4)])
    puzzle.add_palindrome([(1, 6), (2, 6), (2, 5), (3, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(8, 7), (7, 6), (8, 6), (8, 5), (7, 4)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 2), (5, 1)])
    puzzle.add_palindrome([(7, 5), (6, 5), (5, 6), (6, 6)])
    puzzle.add_palindrome([(0, 6), (1, 5), (1, 4)])

    return puzzle
