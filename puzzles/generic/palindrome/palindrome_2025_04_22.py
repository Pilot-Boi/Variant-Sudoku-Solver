"""PuzzleMadness Palindrome Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 9],
        [0, 0, 0, 0, 5, 0, 0, 0, 7],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 8],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 5, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 2), (5, 3), (6, 2), (7, 3), (8, 3), (7, 2), (6, 1)])
    puzzle.add_palindrome([(1, 3), (2, 4), (3, 4), (2, 3), (3, 2), (4, 2)])
    puzzle.add_palindrome([(6, 5), (7, 5), (8, 5), (8, 6), (7, 6)])
    puzzle.add_palindrome([(4, 8), (5, 8), (6, 7)])
    puzzle.add_palindrome([(3, 0), (2, 0), (2, 1)])

    return puzzle
