"""PuzzleMadness Palindrome Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 1, 0, 0, 0, 5],
        [0, 3, 0, 0, 2, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 6), (3, 7), (2, 7), (3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_palindrome([(8, 4), (7, 3), (8, 3), (8, 2), (7, 2)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 4), (4, 5), (3, 5)])
    puzzle.add_palindrome([(2, 8), (1, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 1), (4, 0)])
    puzzle.add_palindrome([(6, 2), (5, 2), (4, 1)])

    return puzzle
