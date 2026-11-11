"""PuzzleMadness Palindrome Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 1, 0, 0, 0],
        [0, 0, 7, 0, 0, 9, 0, 3, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (0, 7), (1, 6), (2, 7), (3, 8), (3, 7), (4, 8), (4, 7)])
    puzzle.add_palindrome([(5, 6), (6, 5), (7, 6), (8, 6), (7, 7)])
    puzzle.add_palindrome([(3, 1), (4, 2), (3, 2), (4, 3), (5, 4), (4, 4)])
    puzzle.add_palindrome([(0, 2), (0, 1), (1, 2), (0, 3), (1, 3), (1, 4)])
    puzzle.add_palindrome([(2, 2), (3, 3), (3, 4)])
    puzzle.add_palindrome([(6, 3), (7, 2), (7, 1)])

    return puzzle
