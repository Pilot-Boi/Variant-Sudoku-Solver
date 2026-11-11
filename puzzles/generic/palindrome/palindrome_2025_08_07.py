"""PuzzleMadness Palindrome Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 3, 1, 0, 0],
        [0, 0, 0, 8, 2, 0, 0, 0, 6],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 4), (7, 3), (6, 2), (5, 1), (5, 0), (4, 1), (3, 2)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 3), (1, 4), (1, 3)])
    puzzle.add_palindrome([(2, 4), (1, 5), (1, 6), (0, 6), (1, 7)])
    puzzle.add_palindrome([(4, 4), (5, 5), (6, 6)])
    puzzle.add_palindrome([(4, 6), (4, 5), (5, 6), (6, 7)])

    return puzzle
