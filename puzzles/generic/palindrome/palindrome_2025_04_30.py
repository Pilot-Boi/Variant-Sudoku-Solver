"""PuzzleMadness Palindrome Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 3],
        [0, 0, 7, 1, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (7, 4), (8, 3), (8, 2), (7, 3), (6, 2), (6, 1), (7, 2)])
    puzzle.add_palindrome([(0, 3), (1, 4), (2, 5), (1, 6), (0, 7), (1, 7)])
    puzzle.add_palindrome([(5, 5), (6, 5), (6, 6), (5, 7), (4, 8), (3, 8)])
    puzzle.add_palindrome([(5, 6), (4, 6), (3, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_palindrome([(2, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(2, 2), (3, 1), (3, 0)])

    return puzzle
