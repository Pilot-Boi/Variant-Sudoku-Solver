"""PuzzleMadness Palindrome Sudoku — 2025-01-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 6, 0, 0, 0, 0, 3, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 4), (6, 3), (7, 3), (8, 2), (8, 1), (7, 0), (6, 1)])
    puzzle.add_palindrome([(4, 1), (4, 2), (4, 3), (5, 4), (5, 3)])
    puzzle.add_palindrome([(0, 8), (1, 7), (1, 6), (2, 5), (1, 4)])
    puzzle.add_palindrome([(2, 7), (3, 6), (4, 5), (5, 6)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 3), (2, 2)])
    puzzle.add_palindrome([(2, 1), (1, 2), (1, 3)])

    return puzzle
