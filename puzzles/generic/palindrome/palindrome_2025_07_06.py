"""PuzzleMadness Palindrome Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 9, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 2],
        [0, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 6, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 1), (2, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 4), (3, 3)])
    puzzle.add_palindrome([(3, 1), (4, 2), (5, 1), (6, 0), (6, 1), (7, 0)])
    puzzle.add_palindrome([(5, 3), (5, 2), (6, 2), (7, 1), (8, 1)])
    puzzle.add_palindrome([(1, 7), (2, 6), (2, 5)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2)])

    return puzzle
