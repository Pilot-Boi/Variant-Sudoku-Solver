"""PuzzleMadness Palindrome Sudoku — 2025-04-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 1, 2, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 8, 9, 0, 1],
        [0, 8, 0, 0, 0, 6, 0, 0, 7],
        [5, 3, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 3), (6, 4), (5, 3), (4, 2), (3, 3), (4, 4), (4, 5)])
    puzzle.add_palindrome([(3, 4), (2, 4), (1, 3), (1, 2), (2, 2)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 5), (0, 4), (0, 3)])
    puzzle.add_palindrome([(2, 5), (3, 6), (2, 7), (1, 7)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(7, 5), (8, 6), (8, 7)])

    return puzzle
