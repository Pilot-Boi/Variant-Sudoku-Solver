"""PuzzleMadness Palindrome Sudoku — 2025-12-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 8, 0, 2, 0],
        [0, 9, 8, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [6, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (7, 1), (8, 2), (8, 3), (7, 3), (6, 3), (7, 4)])
    puzzle.add_palindrome([(3, 7), (2, 8), (2, 7), (3, 6), (3, 5), (2, 6)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2), (2, 1), (2, 0)])
    puzzle.add_palindrome([(7, 6), (6, 5), (5, 6), (5, 7), (4, 7)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 2), (2, 3)])
    puzzle.add_palindrome([(4, 6), (5, 5), (6, 4), (5, 3)])

    return puzzle
