"""PuzzleMadness Palindrome Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [7, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 1, 6, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (7, 4), (8, 3), (7, 3), (6, 2), (6, 1), (5, 1)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 3), (1, 3), (0, 2)])
    puzzle.add_palindrome([(2, 0), (2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(0, 4), (1, 4), (0, 5), (1, 6), (2, 7), (1, 8)])
    puzzle.add_palindrome([(4, 3), (5, 3), (4, 2), (3, 1)])
    puzzle.add_palindrome([(4, 5), (3, 4), (2, 5), (2, 6)])
    puzzle.add_palindrome([(5, 6), (6, 6), (5, 5), (6, 5)])

    return puzzle
