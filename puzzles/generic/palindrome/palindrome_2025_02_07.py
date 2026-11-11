"""PuzzleMadness Palindrome Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 2, 1, 0, 0, 0, 0, 0, 0],
        [4, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 4, 3],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (6, 5), (7, 5), (7, 6), (8, 7), (7, 8), (6, 8)])
    puzzle.add_palindrome([(6, 1), (5, 1), (6, 2), (7, 3), (6, 3), (5, 3)])
    puzzle.add_palindrome([(1, 2), (0, 3), (1, 3), (2, 2), (3, 3)])
    puzzle.add_palindrome([(0, 6), (1, 5), (1, 4)])
    puzzle.add_palindrome([(1, 8), (2, 8), (3, 7), (3, 6)])
    puzzle.add_palindrome([(4, 4), (5, 5), (4, 6), (5, 6)])

    return puzzle
