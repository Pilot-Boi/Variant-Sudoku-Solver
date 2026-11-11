"""PuzzleMadness Palindrome Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 6, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 3, 8],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 7, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 8), (8, 8), (8, 7), (7, 6), (6, 5), (6, 4), (6, 3), (6, 2)])
    puzzle.add_palindrome([(5, 7), (4, 7), (5, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 0), (4, 0), (5, 1)])
    puzzle.add_palindrome([(2, 4), (3, 5), (2, 5), (1, 6), (1, 7)])
    puzzle.add_palindrome([(8, 6), (8, 5), (7, 5)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 6)])
    puzzle.add_palindrome([(1, 2), (2, 1), (3, 1)])

    return puzzle
