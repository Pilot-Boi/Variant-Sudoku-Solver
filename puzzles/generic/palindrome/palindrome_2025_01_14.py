"""PuzzleMadness Palindrome Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 1, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 4],
        [8, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 5, 0, 6, 0, 0, 0],
        [3, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 8), (2, 7), (1, 7), (1, 6), (0, 5), (0, 4), (0, 3), (0, 2)])
    puzzle.add_palindrome([(4, 4), (5, 3), (6, 3), (5, 2), (6, 1), (6, 2)])
    puzzle.add_palindrome([(5, 4), (4, 5), (4, 6), (3, 7), (3, 6)])
    puzzle.add_palindrome([(3, 1), (3, 2), (4, 3)])
    puzzle.add_palindrome([(2, 4), (3, 4), (2, 3), (1, 2)])

    return puzzle
