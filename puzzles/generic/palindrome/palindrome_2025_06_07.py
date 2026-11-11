"""PuzzleMadness Palindrome Sudoku — 2025-06-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 2), (6, 3), (7, 3), (8, 2), (7, 1), (6, 0), (5, 0)])
    puzzle.add_palindrome([(5, 5), (4, 5), (5, 6), (6, 7), (7, 7), (8, 7)])
    puzzle.add_palindrome([(1, 4), (2, 5), (3, 4), (2, 3), (3, 2), (3, 3)])
    puzzle.add_palindrome([(7, 4), (6, 5), (7, 6), (6, 6)])
    puzzle.add_palindrome([(0, 1), (0, 2), (1, 3), (2, 4)])
    puzzle.add_palindrome([(3, 7), (2, 7), (2, 6)])

    return puzzle
