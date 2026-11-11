"""PuzzleMadness Palindrome Sudoku — 2025-12-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 1, 7, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 1), (4, 2), (4, 3), (3, 3), (2, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_palindrome([(4, 6), (3, 6), (4, 5), (4, 4), (3, 5)])
    puzzle.add_palindrome([(5, 8), (4, 7), (5, 6), (6, 6), (6, 5)])
    puzzle.add_palindrome([(8, 4), (7, 5), (6, 4), (5, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(1, 6), (2, 5), (3, 4), (2, 4)])
    puzzle.add_palindrome([(7, 7), (7, 6), (8, 5)])
    puzzle.add_palindrome([(1, 4), (0, 5), (0, 6)])

    return puzzle
