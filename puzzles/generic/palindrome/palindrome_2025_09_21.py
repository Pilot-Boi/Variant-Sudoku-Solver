"""PuzzleMadness Palindrome Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 1, 0, 0, 7, 2],
        [0, 0, 3, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 4), (3, 5), (4, 6), (3, 7), (2, 6), (2, 5), (1, 6), (0, 6)])
    puzzle.add_palindrome([(4, 1), (3, 0), (3, 1), (2, 2), (1, 2), (0, 2)])
    puzzle.add_palindrome([(4, 5), (5, 4), (5, 5), (6, 4), (7, 3), (6, 3)])
    puzzle.add_palindrome([(6, 2), (7, 1), (7, 2), (8, 3), (7, 4)])
    puzzle.add_palindrome([(6, 6), (7, 5), (8, 4)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 8)])
    puzzle.add_palindrome([(3, 3), (4, 2), (5, 1)])

    return puzzle
