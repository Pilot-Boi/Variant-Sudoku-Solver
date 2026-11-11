"""PuzzleMadness Palindrome Sudoku — 2025-11-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 9, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 3, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 9, 0, 0, 4, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 8), (4, 8), (5, 8), (6, 8), (5, 7), (6, 6), (6, 7), (7, 6)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 4), (5, 5), (5, 6)])
    puzzle.add_palindrome([(4, 5), (3, 6), (3, 7), (2, 8), (1, 7)])
    puzzle.add_palindrome([(7, 2), (8, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(1, 4), (2, 5), (3, 4), (3, 5)])

    return puzzle
