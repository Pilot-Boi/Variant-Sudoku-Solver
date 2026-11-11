"""PuzzleMadness Palindrome Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 1, 6],
        [7, 0, 0, 4, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 7), (2, 7), (1, 6), (0, 5), (0, 4), (1, 4), (2, 3)])
    puzzle.add_palindrome([(6, 4), (7, 3), (6, 2), (5, 1), (6, 1), (7, 1)])
    puzzle.add_palindrome([(6, 7), (5, 6), (4, 6), (3, 5), (2, 5), (1, 5)])
    puzzle.add_palindrome([(7, 4), (6, 5), (5, 4), (4, 3), (3, 3)])
    puzzle.add_palindrome([(0, 1), (1, 2), (1, 3)])
    puzzle.add_palindrome([(2, 2), (3, 1), (4, 1)])

    return puzzle
