"""PuzzleMadness Palindrome Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 1, 0],
        [0, 0, 0, 7, 4, 0, 0, 9, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (0, 0), (1, 1), (2, 1), (3, 2), (3, 1), (3, 0)])
    puzzle.add_palindrome([(6, 0), (6, 1), (6, 2), (7, 3), (7, 4), (7, 5)])
    puzzle.add_palindrome([(8, 7), (7, 8), (6, 8), (5, 7), (5, 6)])
    puzzle.add_palindrome([(4, 2), (3, 3), (3, 4)])
    puzzle.add_palindrome([(3, 6), (2, 6), (1, 5)])
    puzzle.add_palindrome([(2, 7), (3, 8), (4, 8)])

    return puzzle
