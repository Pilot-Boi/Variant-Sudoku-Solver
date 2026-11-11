"""PuzzleMadness Palindrome Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 5, 0, 0, 0, 0, 2],
        [0, 0, 8, 0, 0, 3, 0, 4, 0],
        [4, 0, 0, 9, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 6), (1, 6), (0, 6), (0, 5), (1, 5), (2, 4), (1, 3)])
    puzzle.add_palindrome([(6, 1), (5, 0), (5, 1), (6, 2), (6, 3), (7, 4)])
    puzzle.add_palindrome([(4, 1), (4, 0), (3, 0), (2, 1), (1, 1), (0, 2)])
    puzzle.add_palindrome([(6, 6), (5, 6), (6, 5), (5, 4)])
    puzzle.add_palindrome([(4, 5), (3, 4), (2, 5), (3, 6)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 3), (1, 2)])

    return puzzle
