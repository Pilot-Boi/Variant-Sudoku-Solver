"""PuzzleMadness Palindrome Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 3, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 4, 0, 0],
        [0, 4, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 0), (4, 0), (3, 0), (2, 1), (1, 1), (0, 1), (1, 0)])
    puzzle.add_palindrome([(7, 5), (6, 5), (5, 4), (5, 3), (4, 4)])
    puzzle.add_palindrome([(4, 1), (3, 2), (2, 2), (1, 3), (0, 3), (1, 2)])
    puzzle.add_palindrome([(4, 6), (3, 6), (3, 5), (2, 4), (1, 4)])
    puzzle.add_palindrome([(0, 4), (0, 5), (1, 6), (1, 7)])
    puzzle.add_palindrome([(5, 8), (6, 7), (6, 6)])

    return puzzle
