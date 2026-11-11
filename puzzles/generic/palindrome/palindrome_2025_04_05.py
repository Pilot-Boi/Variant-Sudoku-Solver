"""PuzzleMadness Palindrome Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 9, 0, 4, 0],
        [0, 0, 0, 0, 7, 0, 0, 8, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (6, 6), (7, 5), (7, 6), (8, 6), (8, 5), (7, 4)])
    puzzle.add_palindrome([(4, 6), (5, 6), (4, 5), (3, 5), (2, 4)])
    puzzle.add_palindrome([(1, 6), (1, 7), (2, 8), (3, 7), (4, 8), (5, 8)])
    puzzle.add_palindrome([(6, 3), (5, 3), (6, 4), (6, 5), (5, 4)])
    puzzle.add_palindrome([(2, 2), (2, 3), (3, 4)])
    puzzle.add_palindrome([(6, 2), (5, 2), (4, 1)])
    puzzle.add_palindrome([(8, 1), (7, 2), (8, 3), (7, 3)])

    return puzzle
