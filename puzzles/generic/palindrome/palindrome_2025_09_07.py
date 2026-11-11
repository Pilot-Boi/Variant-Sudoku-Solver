"""PuzzleMadness Palindrome Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 9, 0, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [8, 0, 1, 4, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 6), (6, 5), (5, 6), (5, 7), (4, 8), (3, 8)])
    puzzle.add_palindrome([(3, 2), (4, 3), (5, 4), (6, 3), (6, 2), (6, 1)])
    puzzle.add_palindrome([(2, 5), (3, 6), (4, 6), (5, 5), (6, 4)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 0), (4, 0)])
    puzzle.add_palindrome([(0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(5, 0), (6, 0), (7, 1)])

    return puzzle
