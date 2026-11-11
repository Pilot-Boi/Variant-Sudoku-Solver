"""PuzzleMadness Palindrome Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 5, 4, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 3, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (4, 3), (3, 3), (2, 3), (1, 2), (1, 1), (0, 2), (1, 3)])
    puzzle.add_palindrome([(2, 0), (2, 1), (3, 0), (4, 0), (3, 1)])
    puzzle.add_palindrome([(8, 4), (8, 5), (7, 5), (6, 6), (5, 7), (4, 7)])
    puzzle.add_palindrome([(1, 6), (0, 6), (1, 5), (2, 4)])
    puzzle.add_palindrome([(7, 2), (6, 3), (5, 3)])
    puzzle.add_palindrome([(7, 1), (8, 2), (7, 3), (6, 4)])

    return puzzle
