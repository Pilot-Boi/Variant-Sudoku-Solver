"""PuzzleMadness Palindrome Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 5, 8, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 7), (2, 6), (2, 5), (2, 4), (3, 5), (3, 4), (4, 5), (4, 6)])
    puzzle.add_palindrome([(3, 1), (2, 2), (2, 3), (1, 2), (0, 3), (0, 4)])
    puzzle.add_palindrome([(1, 7), (2, 8), (3, 7), (4, 7), (4, 8)])
    puzzle.add_palindrome([(5, 0), (4, 0), (3, 0), (2, 1), (1, 1), (0, 2)])
    puzzle.add_palindrome([(1, 5), (0, 6), (0, 7)])
    puzzle.add_palindrome([(5, 3), (6, 2), (7, 3), (8, 2)])

    return puzzle
