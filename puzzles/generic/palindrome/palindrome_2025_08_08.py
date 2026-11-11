"""PuzzleMadness Palindrome Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 7, 1, 0],
        [0, 1, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 6), (3, 5), (2, 6), (2, 5), (1, 6), (0, 5), (0, 6), (1, 7)])
    puzzle.add_palindrome([(2, 3), (1, 4), (1, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(4, 6), (5, 7), (6, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(5, 4), (4, 4), (5, 3), (6, 4), (7, 5), (7, 6)])
    puzzle.add_palindrome([(6, 2), (6, 1), (5, 0)])
    puzzle.add_palindrome([(1, 0), (2, 1), (3, 1)])
    puzzle.add_palindrome([(3, 4), (4, 3), (5, 2), (4, 2)])

    return puzzle
