"""PuzzleMadness Palindrome Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 5, 1],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (4, 6), (4, 7), (5, 8), (6, 8), (6, 7), (7, 8)])
    puzzle.add_palindrome([(0, 5), (1, 4), (2, 3), (3, 2), (3, 1), (2, 1)])
    puzzle.add_palindrome([(4, 4), (5, 3), (6, 2), (7, 2), (6, 3)])
    puzzle.add_palindrome([(5, 6), (6, 6), (7, 6), (8, 5), (8, 4), (7, 4)])
    puzzle.add_palindrome([(3, 3), (4, 3), (4, 2)])
    puzzle.add_palindrome([(1, 2), (0, 2), (1, 3), (0, 3)])
    puzzle.add_palindrome([(4, 1), (3, 0), (2, 0)])

    return puzzle
