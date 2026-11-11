"""PuzzleMadness Palindrome Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 6, 9],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 8, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 0), (8, 1), (7, 0), (6, 1), (5, 2), (5, 1), (4, 2), (3, 2)])
    puzzle.add_palindrome([(6, 7), (5, 7), (5, 6), (4, 5), (3, 5), (2, 6)])
    puzzle.add_palindrome([(4, 4), (5, 5), (6, 6), (7, 5), (8, 6), (7, 7)])
    puzzle.add_palindrome([(6, 2), (7, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_palindrome([(0, 6), (1, 6), (1, 5)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 6), (4, 7)])

    return puzzle
