"""PuzzleMadness Palindrome Sudoku — 2025-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 5, 0, 0, 8, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [1, 0, 0, 0, 2, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (3, 3), (4, 4), (5, 5), (6, 6), (5, 7), (6, 7), (6, 8)])
    puzzle.add_palindrome([(2, 3), (1, 4), (0, 5), (1, 6), (0, 7), (0, 8)])
    puzzle.add_palindrome([(7, 5), (6, 4), (5, 4), (4, 3), (5, 3)])
    puzzle.add_palindrome([(6, 0), (7, 0), (6, 1), (5, 1), (5, 2)])
    puzzle.add_palindrome([(3, 5), (3, 4), (2, 4)])
    puzzle.add_palindrome([(7, 2), (7, 3), (8, 4)])
    puzzle.add_palindrome([(2, 8), (3, 7), (4, 7)])

    return puzzle
