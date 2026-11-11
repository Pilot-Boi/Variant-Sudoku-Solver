"""PuzzleMadness Palindrome Sudoku — 2025-07-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 1, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [2, 0, 7, 8, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 3), (7, 2), (7, 3), (6, 3), (6, 2), (5, 3), (4, 4)])
    puzzle.add_palindrome([(1, 4), (0, 3), (1, 2), (2, 2), (2, 1)])
    puzzle.add_palindrome([(3, 3), (4, 3), (5, 2), (6, 1), (5, 1)])
    puzzle.add_palindrome([(4, 6), (3, 5), (3, 4), (2, 3), (1, 3), (2, 4)])
    puzzle.add_palindrome([(6, 5), (6, 6), (7, 7)])
    puzzle.add_palindrome([(7, 8), (6, 7), (5, 7)])

    return puzzle
