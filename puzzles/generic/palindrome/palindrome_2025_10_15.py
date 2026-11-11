"""PuzzleMadness Palindrome Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 3, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 8, 0],
        [9, 0, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 6), (4, 5), (3, 5), (3, 6), (2, 7), (2, 6)])
    puzzle.add_palindrome([(4, 4), (5, 3), (4, 3), (5, 2), (6, 2), (6, 3)])
    puzzle.add_palindrome([(3, 4), (2, 4), (1, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 2), (3, 3)])
    puzzle.add_palindrome([(6, 1), (7, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(7, 8), (6, 8), (5, 7), (4, 7)])

    return puzzle
