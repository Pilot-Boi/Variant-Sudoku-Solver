"""PuzzleMadness Palindrome Sudoku — 2025-05-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 9],
        [7, 5, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 9, 3, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (1, 7), (2, 7), (3, 6), (2, 5), (3, 4), (3, 3), (4, 3)])
    puzzle.add_palindrome([(2, 0), (2, 1), (2, 2), (1, 3), (0, 4), (0, 5)])
    puzzle.add_palindrome([(7, 3), (8, 4), (8, 5), (7, 6), (6, 7), (6, 6)])
    puzzle.add_palindrome([(3, 5), (4, 4), (4, 5), (5, 6), (6, 5), (6, 4)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1)])
    puzzle.add_palindrome([(3, 7), (3, 8), (2, 8)])
    puzzle.add_palindrome([(6, 1), (5, 2), (5, 3)])

    return puzzle
