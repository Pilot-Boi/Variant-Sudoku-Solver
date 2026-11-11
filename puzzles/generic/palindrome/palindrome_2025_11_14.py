"""PuzzleMadness Palindrome Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 2, 0, 8, 0, 7, 0, 3, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 2, 0, 0],
        [0, 0, 9, 0, 6, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 2), (1, 1), (0, 2), (0, 3), (1, 3), (0, 4), (1, 4)])
    puzzle.add_palindrome([(7, 7), (8, 7), (7, 6), (7, 5), (6, 4)])
    puzzle.add_palindrome([(5, 0), (6, 1), (5, 1), (6, 2), (5, 3), (4, 4)])
    puzzle.add_palindrome([(2, 5), (1, 5), (1, 6), (0, 7), (0, 8)])
    puzzle.add_palindrome([(3, 5), (3, 4), (2, 3), (2, 4)])
    puzzle.add_palindrome([(4, 5), (5, 5), (6, 6), (5, 7)])

    return puzzle
