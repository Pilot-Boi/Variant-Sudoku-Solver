"""PuzzleMadness Palindrome Sudoku — 2025-05-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
        [0, 0, 2, 0, 1, 0, 3, 0, 0],
        [0, 9, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 6],
        [0, 0, 0, 2, 0, 3, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 7), (2, 7), (2, 8), (3, 7), (3, 6), (3, 5), (3, 4)])
    puzzle.add_palindrome([(3, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
    puzzle.add_palindrome([(7, 2), (7, 3), (6, 4), (5, 5), (5, 6)])
    puzzle.add_palindrome([(3, 1), (4, 2), (5, 3), (6, 2)])
    puzzle.add_palindrome([(6, 5), (7, 5), (6, 6), (7, 7)])
    puzzle.add_palindrome([(8, 7), (7, 6), (8, 5), (7, 4)])

    return puzzle
