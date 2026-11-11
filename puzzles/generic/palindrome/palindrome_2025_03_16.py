"""PuzzleMadness Palindrome Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 4, 3, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 2, 0, 0, 0, 7, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 0, 0, 6, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 4), (4, 3), (3, 2), (2, 2), (2, 1), (3, 1)])
    puzzle.add_palindrome([(2, 7), (1, 6), (0, 5), (0, 4), (1, 4)])
    puzzle.add_palindrome([(5, 7), (5, 6), (4, 5), (3, 5), (3, 4)])
    puzzle.add_palindrome([(6, 4), (5, 4), (6, 5), (7, 6), (7, 5), (8, 6)])
    puzzle.add_palindrome([(1, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(4, 2), (5, 2), (6, 3), (7, 3)])

    return puzzle
