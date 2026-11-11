"""PuzzleMadness Palindrome Sudoku — 2025-09-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 4, 7, 0],
        [0, 0, 0, 0, 0, 3, 2, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (5, 5), (4, 5), (3, 5), (2, 4), (2, 3), (1, 2)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 1), (3, 0), (4, 1)])
    puzzle.add_palindrome([(1, 6), (2, 5), (3, 6), (2, 7), (3, 8), (4, 7)])
    puzzle.add_palindrome([(5, 4), (6, 4), (7, 3)])
    puzzle.add_palindrome([(6, 2), (5, 3), (4, 3)])

    return puzzle
