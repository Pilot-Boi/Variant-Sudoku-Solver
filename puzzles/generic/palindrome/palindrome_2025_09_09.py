"""PuzzleMadness Palindrome Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 1, 0, 9, 8, 0, 0, 0],
        [9, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 4, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (5, 3), (6, 4), (5, 5), (5, 6), (6, 6), (5, 7)])
    puzzle.add_palindrome([(1, 5), (2, 5), (1, 6), (0, 5), (0, 6), (0, 7)])
    puzzle.add_palindrome([(3, 3), (4, 2), (5, 2), (6, 3), (6, 2)])
    puzzle.add_palindrome([(2, 1), (1, 2), (0, 3), (1, 4)])
    puzzle.add_palindrome([(3, 0), (2, 0), (3, 1), (2, 2)])

    return puzzle
