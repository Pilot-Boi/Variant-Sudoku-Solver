"""PuzzleMadness Palindrome Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 7],
        [8, 5, 7, 0, 0, 0, 2, 0, 3],
        [0, 0, 0, 0, 0, 6, 0, 4, 0],
        [6, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (6, 5), (7, 5), (6, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_palindrome([(4, 4), (5, 5), (4, 6), (3, 5), (2, 4), (1, 3)])
    puzzle.add_palindrome([(7, 4), (7, 3), (6, 3), (6, 2), (5, 1)])
    puzzle.add_palindrome([(8, 5), (7, 6), (6, 7)])
    puzzle.add_palindrome([(5, 2), (4, 2), (4, 3)])

    return puzzle
