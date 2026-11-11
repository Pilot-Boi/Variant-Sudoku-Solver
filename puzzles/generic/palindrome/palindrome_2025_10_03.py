"""PuzzleMadness Palindrome Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 8, 0],
        [7, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 3, 0, 0, 8, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 7), (8, 7), (7, 8), (6, 7), (5, 6), (5, 7), (4, 6), (5, 5)])
    puzzle.add_palindrome([(4, 2), (4, 1), (5, 2), (6, 2), (5, 3)])
    puzzle.add_palindrome([(5, 8), (4, 8), (3, 8), (2, 7), (1, 6), (1, 7)])
    puzzle.add_palindrome([(4, 3), (3, 4), (3, 5), (2, 5), (1, 5)])
    puzzle.add_palindrome([(7, 4), (7, 3), (8, 2), (8, 1)])
    puzzle.add_palindrome([(1, 3), (2, 2), (3, 1)])
    puzzle.add_palindrome([(1, 1), (1, 2), (0, 3), (0, 4)])

    return puzzle
