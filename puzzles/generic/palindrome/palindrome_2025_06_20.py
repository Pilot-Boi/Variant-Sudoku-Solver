"""PuzzleMadness Palindrome Sudoku — 2025-06-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 4, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 2],
        [0, 0, 5, 0, 0, 9, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 5), (3, 6), (4, 7), (3, 8), (2, 8), (2, 7), (3, 7)])
    puzzle.add_palindrome([(5, 6), (6, 6), (7, 6), (8, 5), (7, 4), (6, 5)])
    puzzle.add_palindrome([(2, 1), (3, 2), (4, 2), (3, 3), (4, 3), (5, 4)])
    puzzle.add_palindrome([(3, 4), (2, 3), (1, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(0, 7), (1, 6), (0, 5), (1, 5)])
    puzzle.add_palindrome([(5, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(5, 2), (6, 3), (7, 3)])

    return puzzle
