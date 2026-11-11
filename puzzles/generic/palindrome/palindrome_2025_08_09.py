"""PuzzleMadness Palindrome Sudoku — 2025-08-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 2, 0, 6, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 8, 4, 0, 0, 2, 0],
        [7, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (4, 2), (4, 1), (5, 1), (6, 0), (7, 0), (8, 0), (7, 1)])
    puzzle.add_palindrome([(6, 2), (7, 2), (7, 3), (6, 4), (5, 3)])
    puzzle.add_palindrome([(5, 6), (4, 6), (3, 7), (2, 8), (2, 7), (1, 7)])
    puzzle.add_palindrome([(3, 1), (2, 0), (1, 0)])
    puzzle.add_palindrome([(4, 3), (3, 4), (2, 3), (1, 4)])

    return puzzle
