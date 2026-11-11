"""PuzzleMadness Palindrome Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 5],
        [7, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 6), (8, 7), (7, 6), (7, 5), (6, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(4, 0), (4, 1), (5, 1), (6, 0), (7, 0), (7, 1)])
    puzzle.add_palindrome([(2, 4), (1, 3), (2, 3), (3, 4), (4, 5), (3, 5)])
    puzzle.add_palindrome([(2, 7), (3, 6), (4, 6), (5, 5), (6, 6)])
    puzzle.add_palindrome([(3, 1), (3, 0), (2, 1), (1, 0)])
    puzzle.add_palindrome([(8, 2), (8, 3), (7, 4)])

    return puzzle
