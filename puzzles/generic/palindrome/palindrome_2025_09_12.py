"""PuzzleMadness Palindrome Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 2, 0, 0],
        [3, 0, 0, 0, 7, 4, 0, 5, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 7, 3, 0, 9, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (7, 2), (6, 2), (5, 1), (5, 0), (4, 0), (3, 1)])
    puzzle.add_palindrome([(4, 1), (4, 2), (5, 2), (4, 3), (3, 4), (3, 3)])
    puzzle.add_palindrome([(4, 5), (3, 6), (2, 7), (1, 8), (0, 8)])
    puzzle.add_palindrome([(7, 4), (6, 5), (7, 5), (6, 6), (5, 7), (4, 6)])
    puzzle.add_palindrome([(3, 2), (2, 1), (1, 1)])
    puzzle.add_palindrome([(1, 4), (2, 3), (2, 2)])

    return puzzle
