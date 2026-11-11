"""PuzzleMadness Palindrome Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 0, 9, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 9, 0],
        [6, 0, 0, 0, 8, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (8, 4), (7, 5), (6, 4), (5, 5), (4, 4), (4, 3), (4, 2)])
    puzzle.add_palindrome([(3, 0), (3, 1), (3, 2), (2, 3), (1, 4)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2), (2, 1), (2, 0)])
    puzzle.add_palindrome([(4, 7), (3, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(5, 8), (5, 7), (6, 6), (7, 7)])

    return puzzle
