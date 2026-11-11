"""PuzzleMadness Palindrome Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 1, 0, 2, 0],
        [0, 0, 0, 0, 2, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 4), (7, 4), (8, 5), (7, 6), (6, 6), (6, 7), (7, 7)])
    puzzle.add_palindrome([(7, 2), (6, 2), (5, 2), (6, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(3, 8), (2, 7), (1, 6), (2, 5), (1, 4), (0, 4)])
    puzzle.add_palindrome([(6, 4), (7, 3), (6, 3), (5, 4), (4, 5), (3, 5)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 8)])
    puzzle.add_palindrome([(4, 2), (3, 2), (2, 3), (3, 3)])

    return puzzle
