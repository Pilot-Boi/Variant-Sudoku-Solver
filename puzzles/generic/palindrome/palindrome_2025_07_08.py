"""PuzzleMadness Palindrome Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 7, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [8, 0, 0, 6, 0, 0, 0, 9, 0],
        [0, 0, 0, 2, 0, 8, 0, 7, 0],
        [0, 0, 0, 4, 0, 2, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 6), (8, 6), (7, 7), (6, 7), (5, 8), (4, 8), (3, 7), (3, 8)])
    puzzle.add_palindrome([(5, 1), (6, 0), (6, 1), (5, 2), (4, 3)])
    puzzle.add_palindrome([(4, 7), (4, 6), (3, 6), (2, 5), (2, 4), (1, 5)])
    puzzle.add_palindrome([(3, 2), (3, 1), (2, 2), (1, 2), (0, 1)])
    puzzle.add_palindrome([(7, 5), (6, 6), (5, 7)])
    puzzle.add_palindrome([(8, 2), (7, 2), (6, 3)])

    return puzzle
