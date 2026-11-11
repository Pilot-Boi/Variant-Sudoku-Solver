"""PuzzleMadness Palindrome Sudoku — 2025-03-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 1, 0, 3, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 6, 9, 0],
        [0, 0, 7, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (2, 4), (2, 5), (1, 6), (0, 5), (0, 6), (1, 7), (2, 7)])
    puzzle.add_palindrome([(4, 4), (4, 3), (4, 2), (3, 3), (2, 2), (1, 2)])
    puzzle.add_palindrome([(8, 3), (7, 3), (6, 4), (5, 5), (6, 6), (6, 7)])
    puzzle.add_palindrome([(7, 4), (8, 4), (7, 5), (8, 6), (7, 7), (6, 8)])
    puzzle.add_palindrome([(4, 5), (4, 6), (3, 6)])
    puzzle.add_palindrome([(6, 1), (6, 2), (5, 3)])

    return puzzle
