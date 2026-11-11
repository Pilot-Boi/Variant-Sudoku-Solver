"""PuzzleMadness Palindrome Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [9, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 8],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 0), (5, 0), (4, 0), (3, 0), (2, 1), (1, 2), (2, 3), (3, 2)])
    puzzle.add_palindrome([(0, 4), (0, 5), (1, 6), (2, 7), (2, 6)])
    puzzle.add_palindrome([(1, 8), (2, 8), (3, 7), (3, 6), (4, 7)])
    puzzle.add_palindrome([(6, 3), (5, 3), (4, 2)])
    puzzle.add_palindrome([(7, 6), (6, 5), (6, 4)])
    puzzle.add_palindrome([(4, 8), (5, 7), (6, 7)])

    return puzzle
