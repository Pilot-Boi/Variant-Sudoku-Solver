"""PuzzleMadness Palindrome Sudoku — 2025-12-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 4, 0, 0],
        [7, 6, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 7, 0, 5, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 4), (0, 3), (1, 3), (2, 3), (1, 2), (2, 1), (1, 0), (1, 1)])
    puzzle.add_palindrome([(5, 4), (4, 4), (3, 3), (4, 2), (3, 1), (3, 2)])
    puzzle.add_palindrome([(5, 3), (6, 3), (6, 2), (5, 1), (4, 1), (3, 0)])
    puzzle.add_palindrome([(5, 7), (6, 7), (7, 8)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 6), (1, 7)])

    return puzzle
