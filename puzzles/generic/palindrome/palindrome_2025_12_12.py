"""PuzzleMadness Palindrome Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [0, 0, 7, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 5, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 1, 0, 0, 0, 0, 7, 0],
        [0, 3, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (6, 4), (5, 3), (5, 4), (6, 5), (7, 5), (8, 6), (7, 6)])
    puzzle.add_palindrome([(2, 4), (3, 5), (3, 6), (4, 7), (4, 6)])
    puzzle.add_palindrome([(1, 0), (1, 1), (2, 1), (3, 2), (3, 3)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7), (5, 7), (6, 8)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 6), (1, 6)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 0), (4, 1)])

    return puzzle
