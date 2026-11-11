"""PuzzleMadness Palindrome Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 7, 1, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 8, 0, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 1, 0, 0, 0],
        [0, 5, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 1), (4, 0), (5, 0), (6, 1), (5, 2), (4, 3), (3, 3), (3, 4)])
    puzzle.add_palindrome([(8, 5), (7, 5), (6, 6), (6, 7), (6, 8)])
    puzzle.add_palindrome([(1, 3), (2, 2), (2, 1), (3, 0), (3, 1), (3, 2)])
    puzzle.add_palindrome([(4, 5), (5, 5), (6, 4), (7, 3)])
    puzzle.add_palindrome([(3, 7), (2, 6), (1, 5)])
    puzzle.add_palindrome([(5, 4), (6, 3), (7, 2)])

    return puzzle
