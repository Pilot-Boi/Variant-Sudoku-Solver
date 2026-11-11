"""PuzzleMadness Palindrome Sudoku — 2025-06-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 9, 0, 0, 0, 1, 0],
        [0, 0, 5, 0, 0, 0, 9, 0, 0],
        [0, 0, 6, 7, 0, 0, 0, 0, 8],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 2), (2, 1), (3, 1), (3, 2), (2, 3), (1, 3), (0, 3), (0, 4)])
    puzzle.add_palindrome([(5, 1), (6, 1), (5, 2), (6, 3), (5, 4), (4, 3)])
    puzzle.add_palindrome([(4, 7), (5, 7), (5, 6), (4, 5), (3, 4)])
    puzzle.add_palindrome([(7, 5), (7, 4), (6, 5), (7, 6), (8, 6), (8, 7)])
    puzzle.add_palindrome([(8, 3), (7, 3), (8, 2), (7, 1)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 6), (1, 7)])

    return puzzle
