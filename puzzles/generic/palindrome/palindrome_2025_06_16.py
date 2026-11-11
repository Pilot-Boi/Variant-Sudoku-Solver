"""PuzzleMadness Palindrome Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 7, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 3, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (2, 5), (2, 6), (2, 7), (3, 8), (4, 8), (5, 8), (5, 7)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 3), (6, 2), (5, 1), (4, 1)])
    puzzle.add_palindrome([(6, 6), (7, 6), (6, 5), (5, 6), (5, 5), (4, 4)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 2), (1, 3), (0, 4), (0, 5)])
    puzzle.add_palindrome([(8, 1), (8, 2), (7, 3)])
    puzzle.add_palindrome([(3, 6), (4, 6), (4, 5)])

    return puzzle
