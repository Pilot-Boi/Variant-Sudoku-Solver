"""PuzzleMadness Palindrome Sudoku — 2025-06-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 9, 0, 0, 7, 0],
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 2, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 6), (7, 5), (6, 5), (5, 6), (4, 5), (3, 4), (4, 3), (4, 2)])
    puzzle.add_palindrome([(0, 8), (0, 7), (0, 6), (1, 5), (1, 4), (2, 5)])
    puzzle.add_palindrome([(6, 0), (6, 1), (5, 2), (6, 3), (7, 4), (8, 4)])
    puzzle.add_palindrome([(2, 3), (1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(4, 6), (3, 6), (3, 5)])
    puzzle.add_palindrome([(1, 6), (2, 6), (3, 7), (4, 8)])

    return puzzle
