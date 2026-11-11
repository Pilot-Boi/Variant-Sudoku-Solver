"""PuzzleMadness Palindrome Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [2, 0, 0, 7, 4, 6, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 2],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 4), (5, 3), (5, 2), (4, 3), (3, 2), (3, 3), (2, 2)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7), (5, 8), (4, 7), (3, 6)])
    puzzle.add_palindrome([(6, 0), (6, 1), (6, 2), (7, 3), (7, 4), (8, 3)])
    puzzle.add_palindrome([(4, 5), (3, 5), (2, 4)])
    puzzle.add_palindrome([(1, 6), (2, 6), (3, 7)])
    puzzle.add_palindrome([(1, 3), (1, 2), (0, 2)])

    return puzzle
