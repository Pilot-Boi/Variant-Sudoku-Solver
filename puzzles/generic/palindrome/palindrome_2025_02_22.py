"""PuzzleMadness Palindrome Sudoku — 2025-02-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 5, 0, 0, 0, 2],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 0, 4, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 6, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 8), (3, 8), (4, 8), (5, 7), (6, 6), (7, 6), (8, 6), (7, 5)])
    puzzle.add_palindrome([(2, 5), (3, 6), (4, 6), (3, 5), (4, 4), (3, 3)])
    puzzle.add_palindrome([(7, 2), (6, 1), (6, 2), (5, 3), (4, 2), (4, 3)])
    puzzle.add_palindrome([(1, 5), (0, 6), (0, 7)])
    puzzle.add_palindrome([(6, 4), (5, 5), (5, 6)])

    return puzzle
