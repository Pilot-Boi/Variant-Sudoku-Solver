"""PuzzleMadness Palindrome Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 9],
        [1, 4, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 9, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 1],
        [0, 0, 4, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 7, 0, 5, 2, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (1, 7), (2, 8), (2, 7), (3, 7), (4, 8), (5, 8)])
    puzzle.add_palindrome([(5, 7), (4, 6), (5, 5), (6, 6), (6, 7), (6, 8)])
    puzzle.add_palindrome([(7, 8), (8, 7), (7, 6), (6, 5), (6, 4)])
    puzzle.add_palindrome([(6, 1), (7, 2), (8, 3)])
    puzzle.add_palindrome([(4, 4), (4, 3), (3, 2), (2, 1)])
    puzzle.add_palindrome([(4, 1), (5, 2), (6, 3), (5, 3)])

    return puzzle
