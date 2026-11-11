"""PuzzleMadness Palindrome Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 6, 3, 0, 0, 0],
        [0, 0, 2, 0, 5, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [7, 0, 8, 2, 0, 9, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 5],
        [0, 0, 1, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (6, 4), (7, 4), (7, 5), (8, 6), (8, 7), (8, 8), (7, 7)])
    puzzle.add_palindrome([(1, 7), (2, 8), (3, 8), (3, 7), (3, 6)])
    puzzle.add_palindrome([(2, 4), (1, 3), (0, 3), (0, 2), (1, 2)])
    puzzle.add_palindrome([(6, 6), (6, 7), (5, 6), (4, 5)])
    puzzle.add_palindrome([(3, 3), (4, 3), (4, 2)])
    puzzle.add_palindrome([(2, 1), (2, 0), (3, 0)])

    return puzzle
