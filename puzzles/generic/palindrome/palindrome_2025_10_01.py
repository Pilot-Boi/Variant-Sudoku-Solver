"""PuzzleMadness Palindrome Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 5, 0, 0, 0, 1, 6],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 4, 7, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (1, 7), (2, 8), (3, 7), (4, 7), (5, 8), (4, 8)])
    puzzle.add_palindrome([(2, 4), (2, 3), (3, 3), (4, 2), (5, 1), (5, 2)])
    puzzle.add_palindrome([(8, 6), (7, 6), (6, 6), (7, 5), (6, 4), (7, 4)])
    puzzle.add_palindrome([(0, 4), (0, 3), (0, 2), (1, 1), (2, 0)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(4, 5), (3, 5), (4, 6), (5, 7)])
    puzzle.add_palindrome([(1, 5), (0, 5), (1, 6), (2, 7)])

    return puzzle
