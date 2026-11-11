"""PuzzleMadness Palindrome Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 9],
        [0, 7, 0, 0, 6, 0, 0, 5, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [0, 1, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 5, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 3), (7, 3), (6, 4), (5, 3), (4, 2), (5, 2), (6, 2)])
    puzzle.add_palindrome([(4, 6), (5, 6), (6, 5), (5, 4), (4, 3), (3, 4)])
    puzzle.add_palindrome([(2, 2), (3, 3), (2, 4), (1, 5), (0, 6)])
    puzzle.add_palindrome([(6, 6), (5, 7), (4, 8)])
    puzzle.add_palindrome([(2, 5), (1, 6), (1, 7)])
    puzzle.add_palindrome([(3, 8), (3, 7), (2, 6)])

    return puzzle
