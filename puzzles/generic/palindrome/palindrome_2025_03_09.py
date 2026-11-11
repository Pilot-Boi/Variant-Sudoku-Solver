"""PuzzleMadness Palindrome Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 9, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 9, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 4],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 7, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 3), (3, 3), (4, 2), (3, 2), (2, 1), (1, 1), (1, 0), (0, 1)])
    puzzle.add_palindrome([(7, 7), (6, 8), (5, 8), (4, 7), (4, 6)])
    puzzle.add_palindrome([(8, 7), (8, 6), (7, 6), (6, 5), (7, 4)])
    puzzle.add_palindrome([(4, 8), (3, 7), (2, 6), (1, 7)])
    puzzle.add_palindrome([(8, 4), (8, 3), (7, 2), (7, 1)])

    return puzzle
