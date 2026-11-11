"""PuzzleMadness Palindrome Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 4, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 2, 0, 0, 9],
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 4, 0],
        [2, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 4)])
    puzzle.add_palindrome([(2, 4), (1, 4), (0, 5), (1, 6), (0, 6), (0, 7)])
    puzzle.add_palindrome([(6, 1), (6, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_palindrome([(5, 7), (4, 6), (3, 5), (2, 6)])
    puzzle.add_palindrome([(1, 3), (2, 2), (3, 3), (4, 2)])

    return puzzle
