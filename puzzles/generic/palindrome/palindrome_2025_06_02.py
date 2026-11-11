"""PuzzleMadness Palindrome Sudoku — 2025-06-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 2, 4, 0, 1, 5],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [8, 0, 0, 2, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 6, 1, 4, 0, 7],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 4, 6],
        [0, 0, 0, 8, 0, 0, 0, 0, 9],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 1), (5, 2), (4, 2), (3, 3), (2, 4), (2, 3), (1, 2)])
    puzzle.add_palindrome([(8, 6), (7, 5), (6, 6), (5, 7), (5, 8), (4, 7)])
    puzzle.add_palindrome([(7, 2), (7, 3), (6, 3), (5, 4), (4, 4)])
    puzzle.add_palindrome([(3, 2), (2, 1), (2, 0)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8)])

    return puzzle
