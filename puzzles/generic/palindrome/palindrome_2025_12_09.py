"""PuzzleMadness Palindrome Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [5, 0, 0, 1, 0, 6, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 8, 9, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 5), (5, 5), (5, 4), (4, 3), (3, 2), (2, 3), (1, 3), (2, 4)])
    puzzle.add_palindrome([(3, 8), (4, 8), (3, 7), (2, 6), (3, 5), (4, 5)])
    puzzle.add_palindrome([(1, 1), (1, 2), (2, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_palindrome([(7, 2), (8, 1), (8, 2), (7, 3), (6, 4)])
    puzzle.add_palindrome([(5, 2), (5, 1), (6, 0)])
    puzzle.add_palindrome([(1, 4), (0, 3), (0, 2)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 8)])

    return puzzle
