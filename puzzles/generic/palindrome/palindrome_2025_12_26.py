"""PuzzleMadness Palindrome Sudoku — 2025-12-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [6, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 6, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 7, 5, 3, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 5), (3, 4), (2, 3), (1, 2), (1, 1), (0, 0), (0, 1)])
    puzzle.add_palindrome([(5, 3), (5, 4), (6, 5), (7, 5), (8, 6)])
    puzzle.add_palindrome([(5, 8), (4, 7), (3, 6), (2, 5), (3, 5), (2, 4)])
    puzzle.add_palindrome([(3, 3), (4, 3), (4, 2)])
    puzzle.add_palindrome([(7, 7), (6, 8), (5, 7), (5, 6)])

    return puzzle
