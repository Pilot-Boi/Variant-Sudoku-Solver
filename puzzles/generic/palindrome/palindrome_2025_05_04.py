"""PuzzleMadness Palindrome Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 5, 8, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 2, 0, 0],
        [0, 4, 0, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 1), (8, 2), (7, 3), (6, 4), (5, 3), (5, 2), (4, 1), (3, 0)])
    puzzle.add_palindrome([(4, 8), (4, 7), (5, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_palindrome([(0, 1), (1, 0), (2, 0), (3, 1), (3, 2), (4, 2)])
    puzzle.add_palindrome([(5, 8), (6, 7), (7, 7)])
    puzzle.add_palindrome([(7, 0), (6, 1), (5, 1)])

    return puzzle
