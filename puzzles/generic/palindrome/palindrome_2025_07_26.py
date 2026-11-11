"""PuzzleMadness Palindrome Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 7, 5, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 7), (3, 6), (2, 5), (1, 6), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_palindrome([(6, 8), (7, 7), (7, 6), (8, 5), (7, 5)])
    puzzle.add_palindrome([(6, 3), (7, 3), (8, 3), (7, 2), (8, 1), (8, 0)])
    puzzle.add_palindrome([(4, 4), (5, 3), (4, 3), (3, 2), (4, 1), (3, 0)])
    puzzle.add_palindrome([(5, 2), (6, 2), (7, 1)])
    puzzle.add_palindrome([(3, 4), (3, 5), (4, 6), (5, 6)])

    return puzzle
