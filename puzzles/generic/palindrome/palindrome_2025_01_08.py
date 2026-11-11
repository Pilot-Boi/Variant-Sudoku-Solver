"""PuzzleMadness Palindrome Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 5, 0, 0, 9, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 4, 6, 0],
        [2, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (4, 4), (5, 5), (4, 6), (3, 5), (2, 4), (1, 3), (2, 2)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 1), (1, 0), (2, 0)])
    puzzle.add_palindrome([(4, 0), (4, 1), (4, 2), (5, 3), (6, 3)])
    puzzle.add_palindrome([(5, 7), (4, 7), (5, 6), (6, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(8, 1), (8, 2), (7, 3)])
    puzzle.add_palindrome([(1, 5), (2, 5), (3, 6), (2, 7)])

    return puzzle
