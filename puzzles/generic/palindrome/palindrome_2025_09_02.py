"""PuzzleMadness Palindrome Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 1, 0, 5, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 5), (5, 4), (6, 4), (7, 5), (8, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_palindrome([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6)])
    puzzle.add_palindrome([(7, 1), (7, 2), (6, 2), (7, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(2, 7), (1, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 4)])
    puzzle.add_palindrome([(6, 8), (6, 7), (5, 6)])
    puzzle.add_palindrome([(4, 2), (4, 3), (5, 3)])

    return puzzle
