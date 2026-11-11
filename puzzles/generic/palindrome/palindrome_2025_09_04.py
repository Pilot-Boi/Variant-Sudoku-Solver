"""PuzzleMadness Palindrome Sudoku — 2025-09-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 3, 2, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 6, 0, 0],
        [5, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 9, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 4), (2, 5), (1, 5), (0, 5), (0, 6), (1, 7), (2, 8)])
    puzzle.add_palindrome([(3, 7), (4, 6), (5, 5), (5, 4), (4, 5)])
    puzzle.add_palindrome([(4, 3), (5, 3), (5, 2), (4, 1), (3, 0)])
    puzzle.add_palindrome([(3, 4), (2, 3), (1, 3), (0, 2), (1, 2), (2, 2)])
    puzzle.add_palindrome([(8, 3), (7, 3), (6, 2), (6, 1)])
    puzzle.add_palindrome([(8, 5), (7, 6), (6, 6)])

    return puzzle
