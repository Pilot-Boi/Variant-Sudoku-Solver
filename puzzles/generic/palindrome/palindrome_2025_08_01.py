"""PuzzleMadness Palindrome Sudoku — 2025-08-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [7, 0, 6, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 7, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 8, 0, 6],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 7), (2, 7), (3, 6), (4, 6), (4, 5), (5, 5), (5, 4)])
    puzzle.add_palindrome([(3, 3), (4, 2), (3, 1), (2, 0), (1, 0), (1, 1)])
    puzzle.add_palindrome([(5, 3), (6, 2), (7, 3), (8, 3), (8, 4)])
    puzzle.add_palindrome([(8, 0), (7, 0), (6, 0), (5, 1), (5, 2)])
    puzzle.add_palindrome([(2, 4), (1, 3), (0, 2)])
    puzzle.add_palindrome([(2, 3), (2, 2), (1, 2)])

    return puzzle
