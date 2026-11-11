"""PuzzleMadness Palindrome Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 1, 0, 0, 6, 0, 0, 8, 0],
        [5, 0, 0, 0, 9, 8, 0, 7, 0],
        [9, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 2), (6, 1), (6, 2), (7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(3, 4), (4, 5), (5, 5), (6, 6), (5, 6)])
    puzzle.add_palindrome([(1, 7), (1, 6), (0, 5), (0, 4), (0, 3)])
    puzzle.add_palindrome([(4, 6), (3, 6), (2, 5), (1, 5)])
    puzzle.add_palindrome([(4, 0), (3, 1), (2, 1)])
    puzzle.add_palindrome([(5, 2), (5, 1), (6, 0)])

    return puzzle
