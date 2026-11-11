"""PuzzleMadness Palindrome Sudoku — 2025-03-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 2, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 2, 0, 0],
        [0, 0, 9, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 4, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 2), (7, 1), (6, 1), (6, 0), (5, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(7, 6), (6, 6), (6, 7), (5, 8), (4, 7)])
    puzzle.add_palindrome([(1, 5), (0, 5), (1, 6), (1, 7), (0, 8)])
    puzzle.add_palindrome([(1, 0), (2, 0), (3, 1)])
    puzzle.add_palindrome([(3, 6), (2, 5), (3, 4), (2, 3)])

    return puzzle
