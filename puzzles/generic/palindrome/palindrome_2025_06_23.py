"""PuzzleMadness Palindrome Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 6, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [0, 0, 0, 5, 0, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 8), (1, 8), (2, 7), (3, 6), (4, 5), (3, 4), (4, 4), (3, 3)])
    puzzle.add_palindrome([(6, 7), (6, 6), (6, 5), (5, 4), (5, 5), (4, 6)])
    puzzle.add_palindrome([(3, 5), (2, 4), (1, 3), (0, 2), (1, 1), (2, 2)])
    puzzle.add_palindrome([(5, 1), (6, 0), (7, 0)])
    puzzle.add_palindrome([(4, 2), (4, 3), (3, 2), (2, 1)])
    puzzle.add_palindrome([(6, 1), (5, 2), (5, 3)])

    return puzzle
