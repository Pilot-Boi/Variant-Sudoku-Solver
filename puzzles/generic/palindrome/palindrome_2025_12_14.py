"""PuzzleMadness Palindrome Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 3, 0, 0, 0, 8],
        [0, 5, 0, 4, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 1), (4, 2), (5, 3), (6, 4), (5, 5), (4, 6), (3, 7), (3, 8)])
    puzzle.add_palindrome([(4, 4), (3, 4), (2, 4), (3, 3), (2, 3), (2, 2)])
    puzzle.add_palindrome([(2, 7), (1, 7), (1, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(1, 2), (2, 1), (3, 1)])
    puzzle.add_palindrome([(6, 5), (7, 5), (8, 6), (8, 7)])

    return puzzle
