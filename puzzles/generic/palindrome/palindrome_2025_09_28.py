"""PuzzleMadness Palindrome Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 1, 0, 3],
        [1, 0, 0, 5, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (5, 4), (4, 4), (4, 3), (3, 2), (2, 2), (3, 1), (2, 0)])
    puzzle.add_palindrome([(6, 2), (7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(4, 5), (5, 5), (5, 6), (4, 6), (3, 7)])
    puzzle.add_palindrome([(7, 5), (7, 4), (6, 3), (5, 2), (4, 2), (5, 1)])
    puzzle.add_palindrome([(1, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(6, 8), (5, 7), (4, 7)])
    puzzle.add_palindrome([(1, 2), (2, 3), (2, 4)])

    return puzzle
