"""PuzzleMadness Palindrome Sudoku — 2025-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 6, 0, 9, 0, 0, 0],
        [0, 1, 0, 0, 0, 8, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 6), (5, 5), (6, 5), (7, 5), (8, 6), (7, 7), (8, 8)])
    puzzle.add_palindrome([(7, 4), (6, 4), (7, 3), (8, 2), (7, 2), (8, 1)])
    puzzle.add_palindrome([(4, 0), (5, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_palindrome([(1, 4), (2, 5), (2, 6)])
    puzzle.add_palindrome([(5, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(3, 1), (4, 2), (5, 3), (6, 3)])

    return puzzle
