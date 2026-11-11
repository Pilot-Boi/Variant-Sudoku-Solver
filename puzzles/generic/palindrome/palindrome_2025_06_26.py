"""PuzzleMadness Palindrome Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 1, 0],
        [0, 0, 0, 6, 5, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 3],
        [1, 7, 4, 0, 0, 0, 5, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (4, 4), (4, 5), (3, 4), (2, 4), (1, 5), (0, 5)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7), (5, 7), (4, 7)])
    puzzle.add_palindrome([(3, 3), (3, 2), (4, 3), (5, 2), (6, 1), (5, 1)])
    puzzle.add_palindrome([(2, 8), (3, 8), (2, 7), (3, 6)])
    puzzle.add_palindrome([(1, 2), (2, 2), (2, 3)])

    return puzzle
