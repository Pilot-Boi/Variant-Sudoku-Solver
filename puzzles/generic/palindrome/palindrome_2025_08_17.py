"""PuzzleMadness Palindrome Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 9, 6],
        [0, 0, 0, 2, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 7, 5, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 7, 8, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 4), (2, 3), (2, 2), (3, 2), (3, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(8, 0), (7, 0), (6, 1), (5, 2), (6, 3), (6, 4)])
    puzzle.add_palindrome([(0, 5), (1, 5), (1, 6), (2, 6), (1, 7)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 6), (4, 7)])
    puzzle.add_palindrome([(7, 4), (8, 3), (7, 2), (8, 2)])

    return puzzle
