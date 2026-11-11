"""PuzzleMadness Palindrome Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 6, 0, 0, 4, 0, 0, 9],
        [8, 0, 1, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 6, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 0), (5, 0), (4, 1), (5, 2), (6, 3), (6, 2), (7, 1)])
    puzzle.add_palindrome([(6, 4), (5, 3), (4, 3), (4, 2), (3, 3)])
    puzzle.add_palindrome([(5, 7), (6, 6), (7, 6), (8, 5), (7, 5)])
    puzzle.add_palindrome([(6, 5), (5, 5), (5, 6)])
    puzzle.add_palindrome([(1, 3), (0, 3), (1, 2), (2, 1)])

    return puzzle
