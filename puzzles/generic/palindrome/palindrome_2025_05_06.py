"""PuzzleMadness Palindrome Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 5, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 6, 0],
        [0, 6, 1, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 4), (2, 5), (3, 6), (3, 7), (2, 8), (1, 7), (0, 6), (0, 7)])
    puzzle.add_palindrome([(7, 5), (6, 5), (6, 4), (5, 3), (4, 3), (5, 4)])
    puzzle.add_palindrome([(1, 1), (1, 0), (2, 1), (3, 2), (2, 3)])
    puzzle.add_palindrome([(8, 7), (7, 7), (7, 6), (8, 5), (8, 4), (7, 4)])
    puzzle.add_palindrome([(3, 5), (4, 5), (5, 6)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 0)])

    return puzzle
