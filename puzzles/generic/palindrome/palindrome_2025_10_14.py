"""PuzzleMadness Palindrome Sudoku — 2025-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 8, 0, 0, 0],
        [0, 1, 0, 3, 0, 0, 8, 0, 0],
        [9, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [8, 0, 0, 0, 0, 3, 0, 2, 0],
        [0, 9, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 5), (8, 6), (7, 7), (7, 6), (6, 5), (6, 4), (5, 4), (4, 3)])
    puzzle.add_palindrome([(0, 8), (1, 7), (2, 6), (3, 7), (3, 6), (2, 5)])
    puzzle.add_palindrome([(5, 0), (5, 1), (5, 2), (6, 1), (7, 0), (7, 1)])
    puzzle.add_palindrome([(7, 5), (8, 4), (8, 3), (7, 2), (6, 2)])
    puzzle.add_palindrome([(5, 5), (5, 6), (4, 7)])
    puzzle.add_palindrome([(4, 0), (3, 0), (2, 1)])

    return puzzle
