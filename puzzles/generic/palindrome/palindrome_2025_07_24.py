"""PuzzleMadness Palindrome Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 2, 3, 7, 0, 0, 1, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 3), (8, 4), (8, 5), (8, 6), (7, 7), (6, 7), (6, 8)])
    puzzle.add_palindrome([(3, 7), (2, 6), (3, 6), (4, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(3, 0), (3, 1), (2, 2), (1, 3), (0, 4)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1)])
    puzzle.add_palindrome([(3, 4), (3, 3), (4, 2), (5, 2)])
    puzzle.add_palindrome([(6, 5), (5, 5), (4, 6), (4, 7)])

    return puzzle
