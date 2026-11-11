"""PuzzleMadness Palindrome Sudoku — 2025-12-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 4, 9, 0, 0, 3, 6],
        [0, 0, 0, 0, 6, 3, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 4, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 3), (4, 4), (3, 4), (3, 5), (2, 4), (1, 3), (0, 3), (1, 2)])
    puzzle.add_palindrome([(7, 7), (6, 7), (6, 6), (5, 7), (5, 6), (6, 5)])
    puzzle.add_palindrome([(8, 2), (8, 3), (7, 2), (6, 1), (5, 0)])
    puzzle.add_palindrome([(5, 3), (4, 2), (3, 1)])
    puzzle.add_palindrome([(2, 5), (1, 5), (0, 6), (0, 7)])

    return puzzle
