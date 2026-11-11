"""PuzzleMadness Palindrome Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 3, 9, 6],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 5, 0, 4, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (4, 5), (3, 6), (2, 6), (2, 7), (1, 6), (0, 5)])
    puzzle.add_palindrome([(8, 2), (7, 3), (6, 2), (5, 1), (6, 1), (5, 0)])
    puzzle.add_palindrome([(4, 3), (5, 4), (6, 4), (6, 3), (5, 2)])
    puzzle.add_palindrome([(3, 2), (3, 3), (2, 4)])
    puzzle.add_palindrome([(7, 5), (7, 6), (8, 6)])
    puzzle.add_palindrome([(4, 7), (5, 7), (6, 6)])

    return puzzle
