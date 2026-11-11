"""PuzzleMadness Palindrome Sudoku — 2025-11-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 3, 8, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 8, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 6), (4, 6), (4, 7), (3, 8), (2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_palindrome([(2, 5), (3, 4), (3, 3), (4, 2), (4, 1), (3, 2)])
    puzzle.add_palindrome([(8, 4), (8, 3), (7, 2), (7, 1), (6, 1)])
    puzzle.add_palindrome([(6, 4), (5, 4), (4, 5), (5, 6), (6, 6), (5, 7)])
    puzzle.add_palindrome([(5, 2), (4, 3), (4, 4)])
    puzzle.add_palindrome([(7, 4), (8, 5), (7, 6), (8, 7)])
    puzzle.add_palindrome([(1, 2), (2, 2), (3, 1), (4, 0)])

    return puzzle
