"""PuzzleMadness Palindrome Sudoku — 2025-03-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 8, 0, 9],
        [0, 0, 0, 0, 0, 6, 4, 0, 0],
        [4, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 2, 5, 0, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 3), (5, 4), (4, 5), (3, 6), (2, 5), (1, 4)])
    puzzle.add_palindrome([(6, 7), (6, 8), (5, 7), (4, 7), (5, 8)])
    puzzle.add_palindrome([(4, 1), (3, 0), (2, 0), (3, 1), (2, 2), (3, 3)])
    puzzle.add_palindrome([(1, 1), (1, 2), (2, 3)])
    puzzle.add_palindrome([(1, 6), (2, 7), (3, 8), (4, 8)])

    return puzzle
