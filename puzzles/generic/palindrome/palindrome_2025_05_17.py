"""PuzzleMadness Palindrome Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 7, 0, 8, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 5, 0, 0],
        [8, 2, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 6), (4, 5), (4, 4), (5, 5), (6, 5), (7, 4), (8, 4)])
    puzzle.add_palindrome([(2, 4), (3, 3), (4, 3), (4, 2), (3, 1)])
    puzzle.add_palindrome([(6, 2), (7, 2), (6, 1), (5, 0), (4, 1), (3, 0)])
    puzzle.add_palindrome([(8, 5), (7, 5), (7, 6)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 6), (3, 5)])
    puzzle.add_palindrome([(1, 3), (1, 2), (2, 3), (3, 2)])

    return puzzle
