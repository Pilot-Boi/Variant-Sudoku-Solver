"""PuzzleMadness Palindrome Sudoku — 2025-10-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 6, 0, 0],
        [9, 0, 8, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (7, 1), (6, 2), (6, 3), (7, 3), (8, 3), (7, 4)])
    puzzle.add_palindrome([(1, 2), (2, 1), (3, 1), (3, 0), (4, 1)])
    puzzle.add_palindrome([(5, 2), (5, 1), (4, 2), (5, 3), (4, 4), (3, 4)])
    puzzle.add_palindrome([(6, 8), (7, 7), (6, 6), (7, 5), (6, 5), (5, 6)])
    puzzle.add_palindrome([(3, 7), (4, 6), (3, 5), (2, 4)])
    puzzle.add_palindrome([(3, 2), (2, 2), (1, 3)])
    puzzle.add_palindrome([(1, 6), (0, 5), (0, 4)])

    return puzzle
