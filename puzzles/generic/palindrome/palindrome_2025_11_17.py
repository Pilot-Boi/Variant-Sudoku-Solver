"""PuzzleMadness Palindrome Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 6],
        [6, 0, 0, 8, 0, 4, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 1, 0, 0, 0, 4, 0],
        [0, 3, 0, 9, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 6), (7, 6), (6, 7), (5, 8), (5, 7), (4, 7)])
    puzzle.add_palindrome([(6, 5), (6, 4), (5, 4), (4, 3), (3, 3)])
    puzzle.add_palindrome([(2, 5), (2, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_palindrome([(8, 2), (7, 3), (6, 3)])
    puzzle.add_palindrome([(1, 2), (1, 3), (0, 2), (0, 3)])
    puzzle.add_palindrome([(7, 2), (6, 2), (5, 1)])

    return puzzle
