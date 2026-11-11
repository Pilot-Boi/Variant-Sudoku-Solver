"""PuzzleMadness Palindrome Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 1, 2, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 1, 0],
        [5, 0, 0, 7, 3, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (4, 4), (3, 3), (3, 4), (2, 4), (2, 3), (3, 2)])
    puzzle.add_palindrome([(5, 2), (6, 3), (7, 3), (8, 2), (7, 1), (8, 1)])
    puzzle.add_palindrome([(0, 7), (1, 7), (1, 6), (2, 5), (1, 5)])
    puzzle.add_palindrome([(6, 4), (6, 5), (7, 6), (8, 6)])
    puzzle.add_palindrome([(2, 1), (3, 1), (4, 0)])
    puzzle.add_palindrome([(6, 6), (5, 5), (5, 4)])

    return puzzle
