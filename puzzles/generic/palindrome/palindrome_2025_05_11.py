"""PuzzleMadness Palindrome Sudoku — 2025-05-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 2, 9, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 1, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (6, 2), (7, 1), (6, 1), (5, 0), (4, 0), (4, 1), (5, 1)])
    puzzle.add_palindrome([(1, 5), (2, 5), (3, 5), (4, 6), (4, 7), (4, 8)])
    puzzle.add_palindrome([(0, 1), (1, 1), (2, 2), (3, 1), (4, 2), (3, 3)])
    puzzle.add_palindrome([(6, 4), (6, 5), (6, 6), (5, 7), (5, 8)])
    puzzle.add_palindrome([(3, 6), (2, 7), (3, 8), (2, 8)])
    puzzle.add_palindrome([(5, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(0, 2), (1, 3), (2, 3)])

    return puzzle
