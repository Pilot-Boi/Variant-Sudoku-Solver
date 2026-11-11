"""PuzzleMadness Palindrome Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 8, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [4, 6, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 4, 0, 0, 2, 0, 0, 0],
        [7, 2, 0, 0, 0, 6, 0, 0, 0],
        [9, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 4), (3, 5), (3, 4), (4, 3), (5, 2), (6, 2), (6, 3)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 6), (3, 7), (3, 8), (4, 8)])
    puzzle.add_palindrome([(4, 4), (4, 5), (5, 5), (5, 6), (6, 5)])
    puzzle.add_palindrome([(3, 3), (2, 2), (1, 1)])
    puzzle.add_palindrome([(2, 3), (1, 3), (0, 2)])

    return puzzle
