"""PuzzleMadness Palindrome Sudoku — 2025-12-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [7, 0, 3, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 6, 0, 0],
        [0, 6, 4, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 7), (5, 8), (4, 7), (3, 6), (3, 5), (2, 5), (2, 6)])
    puzzle.add_palindrome([(5, 6), (4, 6), (5, 7), (6, 6), (7, 5), (7, 4)])
    puzzle.add_palindrome([(7, 1), (6, 1), (6, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1), (5, 2)])
    puzzle.add_palindrome([(3, 2), (4, 2), (5, 3)])
    puzzle.add_palindrome([(1, 7), (0, 6), (1, 5), (2, 4)])

    return puzzle
