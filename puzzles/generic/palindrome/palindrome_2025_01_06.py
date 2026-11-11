"""PuzzleMadness Palindrome Sudoku — 2025-01-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 8, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 8, 0, 6, 5],
        [0, 0, 3, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 3), (4, 2), (3, 1), (2, 2), (1, 2), (1, 1), (2, 1)])
    puzzle.add_palindrome([(2, 5), (3, 5), (4, 6), (5, 5), (6, 4), (5, 4)])
    puzzle.add_palindrome([(5, 3), (6, 3), (6, 2), (7, 1), (7, 0)])
    puzzle.add_palindrome([(3, 8), (4, 7), (3, 6), (2, 7), (1, 8), (0, 7)])
    puzzle.add_palindrome([(2, 6), (1, 5), (1, 4)])
    puzzle.add_palindrome([(1, 7), (1, 6), (0, 5)])
    puzzle.add_palindrome([(8, 5), (7, 6), (6, 6)])

    return puzzle
