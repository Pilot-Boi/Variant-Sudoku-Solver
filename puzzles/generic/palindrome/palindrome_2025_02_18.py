"""PuzzleMadness Palindrome Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 3, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 1, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (7, 4), (8, 4), (8, 5), (7, 6), (8, 7), (7, 7)])
    puzzle.add_palindrome([(7, 3), (6, 2), (6, 1), (5, 0), (6, 0)])
    puzzle.add_palindrome([(6, 6), (5, 6), (4, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(1, 0), (2, 0), (3, 1), (4, 2), (5, 1)])
    puzzle.add_palindrome([(0, 6), (0, 5), (1, 4)])
    puzzle.add_palindrome([(1, 1), (0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(1, 5), (2, 5), (3, 6), (4, 7)])

    return puzzle
