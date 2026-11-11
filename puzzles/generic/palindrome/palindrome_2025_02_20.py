"""PuzzleMadness Palindrome Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 1],
        [0, 0, 0, 0, 0, 5, 0, 3, 0],
        [8, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 0), (0, 1), (0, 2), (1, 2), (2, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_palindrome([(6, 1), (6, 2), (5, 2), (5, 1), (5, 0)])
    puzzle.add_palindrome([(2, 5), (2, 4), (1, 5), (0, 6), (1, 7), (0, 8)])
    puzzle.add_palindrome([(7, 8), (7, 7), (6, 8), (5, 8), (4, 7)])
    puzzle.add_palindrome([(2, 6), (3, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(3, 1), (2, 2), (3, 3), (4, 3)])

    return puzzle
