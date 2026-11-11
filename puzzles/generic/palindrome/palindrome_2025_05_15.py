"""PuzzleMadness Palindrome Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 3, 1, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 9, 2, 7, 0],
        [0, 1, 2, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 5), (8, 6), (7, 5), (6, 5), (5, 6), (4, 6), (4, 7), (5, 8)])
    puzzle.add_palindrome([(1, 1), (2, 0), (2, 1), (3, 1), (4, 2)])
    puzzle.add_palindrome([(2, 2), (1, 3), (2, 4), (3, 5), (4, 5), (3, 4)])
    puzzle.add_palindrome([(5, 5), (5, 4), (6, 4)])
    puzzle.add_palindrome([(4, 3), (5, 2), (6, 1), (7, 2)])
    puzzle.add_palindrome([(2, 5), (3, 6), (2, 7), (3, 8)])

    return puzzle
