"""PuzzleMadness Palindrome Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 8, 7, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 0, 3, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 2, 4, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 3), (1, 4), (2, 4), (3, 4), (3, 5), (2, 6), (1, 6)])
    puzzle.add_palindrome([(6, 8), (5, 8), (5, 7), (6, 6), (5, 6)])
    puzzle.add_palindrome([(3, 3), (4, 4), (5, 5), (6, 4), (7, 5), (6, 5)])
    puzzle.add_palindrome([(8, 7), (7, 6), (8, 6), (8, 5), (7, 4)])
    puzzle.add_palindrome([(1, 1), (1, 2), (2, 3)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 1), (4, 2)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8), (2, 7)])

    return puzzle
