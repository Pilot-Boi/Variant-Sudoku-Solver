"""PuzzleMadness Palindrome Sudoku — 2025-03-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 2, 5, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [6, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 5), (6, 6), (7, 7), (6, 8), (5, 8), (4, 8), (4, 7)])
    puzzle.add_palindrome([(1, 4), (2, 4), (3, 5), (4, 6), (3, 6), (3, 7)])
    puzzle.add_palindrome([(6, 3), (5, 2), (5, 3), (4, 4), (3, 4)])
    puzzle.add_palindrome([(7, 2), (6, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(7, 5), (8, 6), (8, 7)])
    puzzle.add_palindrome([(0, 6), (0, 5), (1, 5)])

    return puzzle
