"""PuzzleMadness Palindrome Sudoku — 2025-02-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 0, 0, 0, 0, 0],
        [1, 0, 9, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [8, 0, 6, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (2, 3), (1, 4), (2, 5), (1, 6), (2, 7), (1, 8), (2, 8)])
    puzzle.add_palindrome([(5, 5), (5, 4), (4, 5), (3, 6), (2, 6)])
    puzzle.add_palindrome([(7, 8), (7, 7), (6, 6), (7, 5), (8, 4), (8, 3)])
    puzzle.add_palindrome([(4, 1), (5, 1), (4, 2), (5, 3), (4, 4), (3, 5)])
    puzzle.add_palindrome([(6, 3), (5, 2), (6, 1), (7, 0)])
    puzzle.add_palindrome([(2, 1), (1, 2), (1, 3)])

    return puzzle
