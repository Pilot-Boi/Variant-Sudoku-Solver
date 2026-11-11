"""PuzzleMadness Palindrome Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 7, 0, 0, 0, 0],
        [1, 0, 9, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 4, 0, 2, 0, 0, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (3, 4), (3, 3), (4, 3), (3, 2), (4, 1), (4, 0), (5, 1)])
    puzzle.add_palindrome([(5, 5), (5, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_palindrome([(5, 6), (4, 5), (3, 6), (2, 7), (1, 7)])
    puzzle.add_palindrome([(1, 6), (0, 5), (1, 5), (2, 6), (2, 5)])
    puzzle.add_palindrome([(3, 0), (3, 1), (2, 2)])
    puzzle.add_palindrome([(0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(4, 7), (5, 8), (6, 8)])

    return puzzle
