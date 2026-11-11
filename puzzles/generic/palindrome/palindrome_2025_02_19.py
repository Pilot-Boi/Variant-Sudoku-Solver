"""PuzzleMadness Palindrome Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 9, 0, 3, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 2, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (4, 1), (4, 2), (4, 3), (3, 2), (2, 1), (1, 0), (2, 0)])
    puzzle.add_palindrome([(2, 4), (3, 5), (4, 6), (4, 7), (3, 6)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(6, 2), (7, 2), (7, 3)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 3)])
    puzzle.add_palindrome([(0, 5), (1, 6), (2, 7)])

    return puzzle
