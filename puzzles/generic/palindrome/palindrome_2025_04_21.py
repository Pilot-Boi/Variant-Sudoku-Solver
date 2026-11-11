"""PuzzleMadness Palindrome Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 9],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [2, 1, 6, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 5), (1, 5), (1, 6), (2, 6), (3, 5), (4, 4), (3, 3)])
    puzzle.add_palindrome([(3, 7), (3, 6), (4, 6), (5, 5), (6, 5), (7, 5)])
    puzzle.add_palindrome([(5, 3), (5, 2), (6, 1), (6, 0), (7, 0)])
    puzzle.add_palindrome([(2, 0), (3, 0), (3, 1), (2, 2), (3, 2)])
    puzzle.add_palindrome([(1, 3), (2, 4), (3, 4)])
    puzzle.add_palindrome([(1, 4), (0, 3), (0, 2)])

    return puzzle
