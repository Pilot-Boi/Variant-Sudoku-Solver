"""PuzzleMadness Palindrome Sudoku — 2025-05-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 8, 9, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 6), (7, 5), (8, 4), (7, 3), (7, 2), (8, 2), (7, 1)])
    puzzle.add_palindrome([(0, 4), (1, 3), (2, 2), (3, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(1, 5), (2, 4), (2, 5), (1, 6), (0, 6)])
    puzzle.add_palindrome([(0, 7), (1, 8), (2, 8), (3, 7), (3, 6), (4, 6)])
    puzzle.add_palindrome([(6, 5), (5, 4), (5, 3)])
    puzzle.add_palindrome([(3, 2), (3, 1), (2, 0), (1, 0)])

    return puzzle
