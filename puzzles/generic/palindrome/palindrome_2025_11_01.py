"""PuzzleMadness Palindrome Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 7, 0, 0, 0, 2, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 3), (1, 2), (2, 3), (2, 2), (3, 3), (3, 4), (4, 3), (4, 4)])
    puzzle.add_palindrome([(6, 5), (6, 6), (6, 7), (5, 6), (5, 5), (4, 6)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 1), (6, 2), (7, 3), (8, 3)])
    puzzle.add_palindrome([(1, 4), (0, 5), (1, 5), (2, 6), (2, 7)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 5)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 8), (1, 7)])
    puzzle.add_palindrome([(5, 4), (5, 3), (4, 2), (3, 2)])

    return puzzle
