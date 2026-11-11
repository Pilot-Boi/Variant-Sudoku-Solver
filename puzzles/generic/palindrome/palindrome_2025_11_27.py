"""PuzzleMadness Palindrome Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 2, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 2, 6, 3, 0, 0, 7],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (0, 7), (0, 6), (0, 5), (1, 4), (2, 5), (3, 4)])
    puzzle.add_palindrome([(8, 6), (7, 7), (6, 6), (5, 7), (4, 6), (4, 5)])
    puzzle.add_palindrome([(7, 0), (6, 1), (7, 2), (8, 3), (7, 4), (6, 3)])
    puzzle.add_palindrome([(4, 7), (3, 7), (3, 6), (2, 6), (1, 5)])
    puzzle.add_palindrome([(3, 0), (2, 1), (1, 2)])
    puzzle.add_palindrome([(6, 4), (5, 3), (6, 2), (5, 2)])
    puzzle.add_palindrome([(6, 7), (5, 8), (4, 8)])

    return puzzle
