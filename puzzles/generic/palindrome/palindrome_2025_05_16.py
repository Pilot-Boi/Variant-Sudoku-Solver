"""PuzzleMadness Palindrome Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 3, 0, 6, 0, 8, 0],
        [1, 2, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 4), (1, 5), (2, 4), (2, 3), (3, 2), (4, 2), (4, 1), (5, 2)])
    puzzle.add_palindrome([(6, 5), (5, 6), (4, 6), (3, 5), (4, 4)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 7), (3, 6), (3, 7)])
    puzzle.add_palindrome([(6, 7), (6, 6), (7, 6), (8, 5), (7, 4), (8, 4)])
    puzzle.add_palindrome([(1, 0), (2, 0), (3, 1)])
    puzzle.add_palindrome([(5, 4), (6, 4), (5, 3), (6, 2)])

    return puzzle
