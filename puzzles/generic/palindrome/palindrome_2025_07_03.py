"""PuzzleMadness Palindrome Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 2, 0, 9, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 8, 7, 0, 4, 0, 0],
        [2, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (3, 3), (2, 4), (1, 3), (0, 2), (1, 1), (2, 1), (1, 0)])
    puzzle.add_palindrome([(3, 0), (4, 0), (5, 0), (6, 1), (6, 2), (7, 1)])
    puzzle.add_palindrome([(1, 4), (1, 5), (2, 6), (2, 7), (3, 7)])
    puzzle.add_palindrome([(8, 4), (8, 5), (7, 6), (6, 6), (5, 6)])
    puzzle.add_palindrome([(7, 3), (7, 2), (8, 2)])
    puzzle.add_palindrome([(4, 1), (5, 2), (5, 3)])

    return puzzle
