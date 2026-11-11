"""PuzzleMadness Palindrome Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 1, 0, 4, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (7, 4), (6, 3), (6, 2), (5, 1), (4, 0), (3, 0)])
    puzzle.add_palindrome([(5, 6), (4, 7), (5, 7), (6, 6), (6, 7)])
    puzzle.add_palindrome([(3, 4), (3, 3), (3, 2), (2, 2), (1, 3)])
    puzzle.add_palindrome([(8, 7), (8, 6), (8, 5), (7, 6), (6, 5), (5, 5)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8)])
    puzzle.add_palindrome([(5, 2), (4, 3), (4, 4)])
    puzzle.add_palindrome([(2, 4), (2, 5), (1, 6), (0, 7)])

    return puzzle
