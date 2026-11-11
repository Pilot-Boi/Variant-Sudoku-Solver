"""PuzzleMadness Palindrome Sudoku — 2025-05-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [6, 3, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 9, 3, 0, 0],
        [8, 5, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (3, 1), (4, 2), (5, 1), (6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_palindrome([(3, 4), (2, 4), (3, 3), (4, 3), (5, 2)])
    puzzle.add_palindrome([(2, 2), (2, 1), (1, 2), (0, 3), (1, 4), (0, 4)])
    puzzle.add_palindrome([(1, 6), (2, 5), (3, 5)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 8), (3, 7)])

    return puzzle
