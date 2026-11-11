"""PuzzleMadness Palindrome Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 2, 0, 0, 4, 0, 0],
        [0, 0, 0, 5, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [1, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
        [0, 0, 0, 1, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 8), (4, 7), (4, 6), (3, 6), (4, 5), (5, 4), (6, 4), (7, 4)])
    puzzle.add_palindrome([(3, 4), (4, 4), (3, 5), (2, 6), (3, 7), (2, 8)])
    puzzle.add_palindrome([(5, 2), (4, 3), (3, 3), (2, 4), (1, 4), (1, 5)])
    puzzle.add_palindrome([(0, 1), (0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(3, 1), (2, 1), (1, 2)])
    puzzle.add_palindrome([(6, 3), (7, 3), (8, 2), (8, 1)])

    return puzzle
