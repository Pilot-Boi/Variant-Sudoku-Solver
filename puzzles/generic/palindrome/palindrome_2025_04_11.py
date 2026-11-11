"""PuzzleMadness Palindrome Sudoku — 2025-04-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 8, 0, 5],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [1, 0, 5, 0, 0, 2, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 6, 0, 0, 3, 0, 0, 1],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 4), (1, 3), (0, 3), (1, 2), (1, 1), (0, 1), (1, 0)])
    puzzle.add_palindrome([(6, 1), (5, 2), (5, 3), (4, 4), (3, 3)])
    puzzle.add_palindrome([(4, 5), (3, 5), (3, 6), (2, 7), (2, 6), (1, 6)])
    puzzle.add_palindrome([(0, 5), (0, 6), (1, 7)])
    puzzle.add_palindrome([(3, 0), (3, 1), (2, 1)])

    return puzzle
