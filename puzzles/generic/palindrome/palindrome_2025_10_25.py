"""PuzzleMadness Palindrome Sudoku — 2025-10-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 5, 0, 4, 0, 0, 0],
        [8, 0, 0, 0, 0, 2, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 8, 0, 0, 5, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 3), (3, 4), (4, 5), (5, 4), (6, 5), (6, 6), (5, 6), (5, 7)])
    puzzle.add_palindrome([(1, 4), (2, 3), (1, 3), (0, 2), (0, 1)])
    puzzle.add_palindrome([(8, 0), (8, 1), (7, 2), (6, 3), (7, 4)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 0), (4, 0)])
    puzzle.add_palindrome([(7, 1), (6, 1), (5, 0)])

    return puzzle
