"""PuzzleMadness Palindrome Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 7, 9, 0, 0, 0, 0],
        [0, 9, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 0, 1],
        [3, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (6, 6), (7, 7), (6, 8), (5, 8), (4, 7), (3, 6)])
    puzzle.add_palindrome([(1, 4), (2, 3), (3, 3), (4, 4), (5, 3)])
    puzzle.add_palindrome([(5, 2), (6, 3), (7, 3), (8, 2), (7, 1), (8, 1)])
    puzzle.add_palindrome([(6, 7), (5, 6), (4, 6)])
    puzzle.add_palindrome([(3, 8), (3, 7), (2, 6), (1, 6)])
    puzzle.add_palindrome([(3, 5), (2, 5), (2, 4)])

    return puzzle
