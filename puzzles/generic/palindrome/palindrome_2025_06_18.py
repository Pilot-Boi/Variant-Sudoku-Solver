"""PuzzleMadness Palindrome Sudoku — 2025-06-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 4],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 6, 0, 5, 0, 3, 0, 0],
        [0, 4, 3, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 1), (1, 1), (2, 0), (3, 0), (3, 1), (4, 2), (5, 3)])
    puzzle.add_palindrome([(3, 7), (2, 8), (2, 7), (3, 6), (3, 5), (2, 4)])
    puzzle.add_palindrome([(4, 7), (5, 7), (6, 7), (7, 6), (8, 5)])
    puzzle.add_palindrome([(5, 4), (6, 3), (5, 2), (4, 1), (4, 0)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 3), (3, 2)])
    puzzle.add_palindrome([(8, 4), (7, 5), (6, 6)])

    return puzzle
