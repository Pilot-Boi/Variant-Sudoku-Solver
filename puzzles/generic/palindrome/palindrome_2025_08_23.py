"""PuzzleMadness Palindrome Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 3, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 9, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 7],
        [0, 1, 8, 0, 0, 0, 0, 0, 0],
        [2, 0, 9, 8, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (4, 3), (3, 3), (2, 3), (2, 2), (1, 1), (0, 0)])
    puzzle.add_palindrome([(6, 2), (5, 3), (5, 4), (6, 4), (7, 5)])
    puzzle.add_palindrome([(8, 7), (7, 6), (6, 5), (5, 5), (4, 5)])
    puzzle.add_palindrome([(4, 2), (3, 2), (2, 1)])
    puzzle.add_palindrome([(6, 6), (5, 6), (4, 7)])

    return puzzle
