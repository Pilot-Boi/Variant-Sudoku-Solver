"""PuzzleMadness Palindrome Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 3, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
        [7, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 8, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (3, 5), (3, 6), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_palindrome([(3, 3), (4, 3), (5, 2), (6, 1), (7, 2)])
    puzzle.add_palindrome([(0, 2), (0, 1), (1, 2), (2, 3), (2, 4)])
    puzzle.add_palindrome([(5, 7), (6, 7), (5, 6), (4, 5)])
    puzzle.add_palindrome([(5, 4), (5, 5), (6, 5)])

    return puzzle
