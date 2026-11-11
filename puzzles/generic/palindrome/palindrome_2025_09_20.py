"""PuzzleMadness Palindrome Sudoku — 2025-09-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 1, 0, 4, 0, 0, 0, 8, 3],
        [8, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 7), (4, 8), (4, 7), (3, 8), (2, 7), (1, 6), (2, 5), (1, 4)])
    puzzle.add_palindrome([(3, 4), (4, 5), (5, 5), (6, 4), (7, 4), (6, 3)])
    puzzle.add_palindrome([(4, 1), (5, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_palindrome([(4, 3), (5, 4), (5, 3), (6, 2), (7, 3), (7, 2)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2)])
    puzzle.add_palindrome([(7, 7), (6, 7), (5, 8)])

    return puzzle
