"""PuzzleMadness Palindrome Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 4, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 2, 0],
        [0, 0, 1, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 4, 6, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 2), (5, 1), (5, 2), (4, 3), (4, 4), (4, 5), (3, 4)])
    puzzle.add_palindrome([(7, 5), (7, 4), (6, 4), (5, 5), (5, 6)])
    puzzle.add_palindrome([(6, 6), (6, 7), (7, 6), (8, 5), (8, 4), (7, 3)])
    puzzle.add_palindrome([(3, 5), (2, 5), (2, 6)])
    puzzle.add_palindrome([(1, 2), (2, 2), (3, 3), (2, 4)])

    return puzzle
