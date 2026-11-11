"""PuzzleMadness Palindrome Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 6],
        [0, 9, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 8), (5, 7), (4, 8), (3, 7), (2, 6), (1, 7), (0, 6), (1, 6)])
    puzzle.add_palindrome([(6, 6), (6, 5), (5, 6), (4, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(3, 2), (4, 3), (3, 4), (2, 3), (1, 4), (0, 3)])
    puzzle.add_palindrome([(4, 0), (4, 1), (3, 1), (2, 0), (1, 1)])
    puzzle.add_palindrome([(2, 4), (2, 5), (3, 5)])
    puzzle.add_palindrome([(6, 1), (7, 2), (8, 3)])

    return puzzle
