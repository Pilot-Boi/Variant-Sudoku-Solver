"""PuzzleMadness Palindrome Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 7, 5, 0, 0, 0, 0, 0, 3],
        [0, 0, 6, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 6, 0, 0, 0, 4],
        [0, 0, 9, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (2, 5), (3, 5), (4, 6), (5, 6), (6, 7), (7, 7)])
    puzzle.add_palindrome([(7, 4), (8, 3), (7, 3), (8, 2), (7, 1), (8, 1)])
    puzzle.add_palindrome([(2, 4), (1, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_palindrome([(1, 2), (1, 1), (2, 0), (3, 0), (3, 1)])
    puzzle.add_palindrome([(7, 6), (6, 6), (5, 5), (4, 5)])
    puzzle.add_palindrome([(6, 2), (5, 1), (5, 0)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 1)])

    return puzzle
