"""PuzzleMadness Palindrome Sudoku — 2025-06-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 6, 1, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 5, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 5, 0, 0, 2, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [2, 3, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (5, 3), (5, 4), (5, 5), (4, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_palindrome([(4, 7), (5, 6), (5, 7), (6, 6), (6, 7), (6, 8)])
    puzzle.add_palindrome([(3, 4), (4, 5), (3, 5), (2, 6), (2, 7), (1, 8)])
    puzzle.add_palindrome([(5, 2), (5, 1), (6, 0), (7, 1)])
    puzzle.add_palindrome([(2, 4), (3, 3), (4, 3)])

    return puzzle
