"""PuzzleMadness Palindrome Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 1, 0, 0, 4, 0],
        [0, 3, 9, 2, 0, 0, 7, 0, 0],
        [0, 0, 0, 9, 0, 0, 4, 3, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 5), (6, 4), (7, 5), (6, 6), (5, 5), (4, 4), (4, 5), (3, 6)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 1), (2, 0), (1, 1)])
    puzzle.add_palindrome([(5, 6), (4, 6), (5, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(7, 4), (8, 3), (7, 2), (6, 2)])
    puzzle.add_palindrome([(3, 5), (2, 6), (1, 5), (2, 4)])
    puzzle.add_palindrome([(1, 2), (2, 2), (2, 3)])

    return puzzle
