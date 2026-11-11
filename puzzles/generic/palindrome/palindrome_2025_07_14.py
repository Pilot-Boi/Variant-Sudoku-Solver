"""PuzzleMadness Palindrome Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 1, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (5, 5), (4, 4), (3, 3), (2, 2), (2, 1), (1, 1)])
    puzzle.add_palindrome([(3, 4), (3, 5), (2, 4), (1, 3), (0, 3)])
    puzzle.add_palindrome([(7, 3), (7, 2), (6, 2), (5, 1), (4, 1), (4, 2)])
    puzzle.add_palindrome([(7, 4), (8, 3), (8, 2)])
    puzzle.add_palindrome([(4, 7), (5, 8), (6, 7), (7, 8)])

    return puzzle
