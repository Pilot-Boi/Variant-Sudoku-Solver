"""PuzzleMadness Palindrome Sudoku — 2025-11-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 4, 0, 0, 7, 0, 0],
        [4, 1, 3, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 2, 5, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 1), (5, 2), (4, 1), (5, 0), (6, 1), (7, 0), (8, 1), (8, 0)])
    puzzle.add_palindrome([(4, 6), (5, 7), (5, 8), (6, 8), (7, 8)])
    puzzle.add_palindrome([(3, 3), (3, 2), (3, 1), (2, 0), (2, 1), (1, 1)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 4), (1, 3)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (2, 5)])
    puzzle.add_palindrome([(7, 6), (8, 6), (7, 5), (6, 4)])

    return puzzle
