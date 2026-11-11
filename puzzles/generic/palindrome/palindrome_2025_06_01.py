"""PuzzleMadness Palindrome Sudoku — 2025-06-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 3, 0, 8, 6, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [8, 6, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (4, 3), (3, 4), (3, 3), (4, 2), (5, 2), (6, 3)])
    puzzle.add_palindrome([(3, 8), (3, 7), (2, 6), (1, 6), (0, 6)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 1), (4, 0), (5, 1)])
    puzzle.add_palindrome([(5, 6), (6, 5), (7, 6), (8, 5), (8, 6), (8, 7)])
    puzzle.add_palindrome([(7, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(1, 4), (2, 5), (3, 5)])
    puzzle.add_palindrome([(6, 7), (5, 8), (4, 8)])

    return puzzle
