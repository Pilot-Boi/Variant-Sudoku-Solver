"""PuzzleMadness Palindrome Sudoku — 2025-04-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [2, 0, 0, 9, 3, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 3, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (4, 7), (4, 8), (3, 7), (2, 7), (2, 6), (2, 5)])
    puzzle.add_palindrome([(1, 3), (2, 2), (3, 2), (2, 1), (3, 0), (3, 1)])
    puzzle.add_palindrome([(0, 4), (1, 4), (1, 5), (0, 6), (1, 7)])
    puzzle.add_palindrome([(5, 7), (6, 8), (6, 7), (5, 6), (5, 5), (6, 6)])
    puzzle.add_palindrome([(2, 3), (2, 4), (3, 4)])
    puzzle.add_palindrome([(7, 2), (6, 2), (5, 1), (4, 1)])

    return puzzle
