"""PuzzleMadness Palindrome Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 8, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 0), (7, 1), (6, 2), (5, 2), (4, 3), (5, 4), (6, 5), (5, 5)])
    puzzle.add_palindrome([(2, 4), (2, 5), (1, 5), (0, 6), (1, 6), (1, 7)])
    puzzle.add_palindrome([(1, 2), (0, 2), (0, 3), (1, 3), (2, 3)])
    puzzle.add_palindrome([(1, 1), (2, 1), (2, 2), (3, 3), (4, 4), (4, 5)])
    puzzle.add_palindrome([(3, 6), (3, 7), (2, 8), (2, 7)])
    puzzle.add_palindrome([(2, 6), (3, 5), (3, 4)])

    return puzzle
