"""PuzzleMadness Palindrome Sudoku — 2025-05-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 2, 3, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 6, 1, 0, 0],
        [0, 7, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 5), (7, 4), (7, 3), (8, 3), (7, 2), (6, 2), (5, 3), (4, 4)])
    puzzle.add_palindrome([(2, 3), (3, 4), (3, 5), (2, 5), (1, 6)])
    puzzle.add_palindrome([(1, 7), (1, 8), (2, 7), (3, 7), (4, 6)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2), (1, 1), (1, 0)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 0), (4, 1)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1)])
    puzzle.add_palindrome([(6, 7), (7, 6), (7, 5)])

    return puzzle
