"""PuzzleMadness Palindrome Sudoku — 2025-01-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 8, 0, 2, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (0, 0), (1, 1), (2, 2), (3, 2), (3, 1), (3, 0)])
    puzzle.add_palindrome([(1, 8), (1, 7), (1, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(7, 4), (8, 4), (8, 3), (7, 2), (6, 2), (6, 1)])
    puzzle.add_palindrome([(4, 7), (3, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(0, 2), (1, 2), (2, 3), (1, 4)])

    return puzzle
