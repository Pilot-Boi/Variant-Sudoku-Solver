"""PuzzleMadness Palindrome Sudoku — 2025-02-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 6, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 6, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 6), (5, 7), (4, 8), (3, 8), (2, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(7, 4), (8, 5), (7, 5), (7, 6), (6, 6)])
    puzzle.add_palindrome([(7, 2), (6, 3), (6, 4), (5, 5), (4, 5)])
    puzzle.add_palindrome([(6, 2), (6, 1), (5, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(1, 1), (0, 2), (0, 3)])
    puzzle.add_palindrome([(4, 4), (5, 3), (5, 2)])
    puzzle.add_palindrome([(1, 3), (1, 2), (2, 3), (3, 2)])

    return puzzle
