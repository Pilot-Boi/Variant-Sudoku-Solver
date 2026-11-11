"""PuzzleMadness Palindrome Sudoku — 2025-03-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 7],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 7, 2, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 3, 0, 0, 0, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 5), (7, 5), (6, 5), (7, 6), (8, 7), (8, 8), (7, 7)])
    puzzle.add_palindrome([(7, 4), (7, 3), (6, 3), (5, 4), (5, 5)])
    puzzle.add_palindrome([(1, 8), (1, 7), (2, 7), (3, 6), (4, 7)])
    puzzle.add_palindrome([(5, 3), (5, 2), (5, 1), (6, 0), (7, 0)])
    puzzle.add_palindrome([(2, 2), (3, 3), (2, 4), (1, 5)])
    puzzle.add_palindrome([(8, 4), (8, 3), (7, 2), (6, 2)])

    return puzzle
