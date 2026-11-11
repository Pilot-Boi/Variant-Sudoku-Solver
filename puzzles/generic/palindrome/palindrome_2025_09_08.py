"""PuzzleMadness Palindrome Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 9, 8, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 7, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (3, 7), (2, 6), (3, 5), (2, 4), (1, 3), (1, 2), (2, 2)])
    puzzle.add_palindrome([(4, 4), (5, 5), (5, 4), (6, 4), (7, 5)])
    puzzle.add_palindrome([(6, 7), (7, 6), (8, 5), (8, 4), (7, 3)])
    puzzle.add_palindrome([(4, 3), (5, 3), (6, 2), (6, 1)])
    puzzle.add_palindrome([(8, 3), (8, 2), (7, 1)])

    return puzzle
