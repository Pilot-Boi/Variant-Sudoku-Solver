"""PuzzleMadness Palindrome Sudoku — 2025-09-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 2, 3, 8, 0, 0, 0],
        [0, 1, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [9, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (7, 4), (8, 3), (8, 2), (7, 1), (6, 0), (5, 1)])
    puzzle.add_palindrome([(4, 4), (3, 5), (4, 5), (5, 6), (6, 6), (5, 7)])
    puzzle.add_palindrome([(3, 3), (2, 2), (1, 3), (0, 2), (0, 3), (1, 4)])
    puzzle.add_palindrome([(0, 7), (1, 8), (2, 7), (3, 6), (2, 5)])
    puzzle.add_palindrome([(5, 3), (4, 2), (4, 1)])
    puzzle.add_palindrome([(7, 6), (6, 5), (5, 4), (6, 4)])

    return puzzle
