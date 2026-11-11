"""PuzzleMadness Palindrome Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [2, 0, 0, 0, 8, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (3, 3), (2, 2), (3, 2), (3, 1), (4, 0), (4, 1)])
    puzzle.add_palindrome([(8, 4), (8, 3), (7, 2), (6, 2), (5, 3)])
    puzzle.add_palindrome([(4, 5), (5, 4), (4, 3), (5, 2), (6, 1), (5, 0)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 8)])
    puzzle.add_palindrome([(2, 6), (3, 5), (2, 4), (1, 3)])
    puzzle.add_palindrome([(5, 6), (5, 5), (6, 4), (7, 4)])

    return puzzle
