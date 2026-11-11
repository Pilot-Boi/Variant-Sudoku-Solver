"""PuzzleMadness Palindrome Sudoku — 2025-01-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 6, 0, 7, 0, 0],
        [5, 8, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 2, 0, 0, 5, 0, 0, 0, 3],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [6, 5, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (3, 5), (4, 5), (5, 5), (4, 6), (3, 6), (2, 6), (1, 7)])
    puzzle.add_palindrome([(4, 7), (5, 6), (5, 7), (6, 8), (6, 7), (7, 6)])
    puzzle.add_palindrome([(2, 4), (3, 4), (4, 3), (4, 2), (5, 2)])
    puzzle.add_palindrome([(1, 2), (1, 3), (0, 4)])
    puzzle.add_palindrome([(3, 0), (2, 0), (1, 1)])
    puzzle.add_palindrome([(4, 0), (5, 1), (6, 1)])

    return puzzle
