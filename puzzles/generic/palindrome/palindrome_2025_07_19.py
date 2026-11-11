"""PuzzleMadness Palindrome Sudoku — 2025-07-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 5, 0, 3, 0, 0, 6],
        [0, 3, 0, 7, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (2, 1), (3, 1), (4, 2), (5, 3), (5, 4), (6, 5)])
    puzzle.add_palindrome([(7, 1), (6, 2), (5, 2), (5, 1), (4, 0)])
    puzzle.add_palindrome([(1, 5), (2, 5), (3, 5), (2, 4), (3, 4), (3, 3)])
    puzzle.add_palindrome([(7, 7), (7, 8), (6, 7), (5, 6), (5, 7), (5, 8)])
    puzzle.add_palindrome([(1, 1), (2, 2), (2, 3)])
    puzzle.add_palindrome([(1, 7), (2, 6), (3, 6)])

    return puzzle
