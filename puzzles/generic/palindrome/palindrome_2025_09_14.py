"""PuzzleMadness Palindrome Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 8, 3, 0],
        [6, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 5, 0, 0],
        [9, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 9, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 4), (7, 5), (8, 5), (7, 6), (6, 7), (5, 8), (6, 8)])
    puzzle.add_palindrome([(7, 0), (7, 1), (6, 2), (5, 3), (4, 2), (3, 2)])
    puzzle.add_palindrome([(3, 1), (3, 0), (2, 1), (1, 2), (2, 3)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 7), (3, 6), (2, 5)])
    puzzle.add_palindrome([(0, 4), (1, 3), (0, 2), (1, 1)])
    puzzle.add_palindrome([(4, 7), (5, 6), (6, 5), (6, 6)])

    return puzzle
