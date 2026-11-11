"""PuzzleMadness Palindrome Sudoku — 2025-12-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [0, 0, 0, 0, 0, 0, 7, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 7), (4, 6), (5, 5), (5, 6), (6, 6), (7, 5), (7, 6)])
    puzzle.add_palindrome([(1, 7), (1, 6), (2, 7), (3, 7), (4, 8)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 1), (3, 0), (2, 0), (1, 1)])
    puzzle.add_palindrome([(4, 4), (4, 5), (5, 4), (6, 5), (6, 4), (7, 3)])
    puzzle.add_palindrome([(1, 4), (0, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5)])
    puzzle.add_palindrome([(8, 6), (8, 5), (7, 4)])

    return puzzle
