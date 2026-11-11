"""PuzzleMadness Palindrome Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 3, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 6, 0, 5, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 5, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 8, 9],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 3), (6, 3), (6, 2), (5, 2), (4, 3), (5, 3), (5, 4), (4, 5)])
    puzzle.add_palindrome([(4, 4), (3, 4), (2, 4), (1, 3), (0, 3)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 5), (6, 6), (7, 6), (8, 7)])
    puzzle.add_palindrome([(2, 2), (3, 3), (4, 2), (5, 1), (4, 1)])
    puzzle.add_palindrome([(1, 7), (0, 6), (0, 5)])
    puzzle.add_palindrome([(5, 8), (5, 7), (6, 7)])

    return puzzle
