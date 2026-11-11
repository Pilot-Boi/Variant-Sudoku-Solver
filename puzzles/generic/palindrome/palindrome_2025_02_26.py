"""PuzzleMadness Palindrome Sudoku — 2025-02-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 6, 0, 0, 4, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 2, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 7, 8, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (5, 4), (4, 5), (5, 5), (4, 6), (3, 6), (2, 5), (1, 5)])
    puzzle.add_palindrome([(7, 6), (7, 5), (6, 5), (5, 6), (5, 7)])
    puzzle.add_palindrome([(4, 1), (5, 1), (5, 2), (6, 3), (7, 4), (8, 3)])
    puzzle.add_palindrome([(2, 3), (1, 2), (1, 3), (2, 4), (3, 4)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 6), (2, 7)])
    puzzle.add_palindrome([(2, 1), (3, 1), (4, 0)])

    return puzzle
