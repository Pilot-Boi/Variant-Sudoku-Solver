"""PuzzleMadness Palindrome Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 9, 0, 0, 6],
        [0, 0, 5, 7, 0, 6, 1, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 0, 7, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (5, 4), (5, 5), (6, 4), (6, 3), (7, 2), (6, 2)])
    puzzle.add_palindrome([(1, 2), (2, 2), (1, 3), (0, 4), (0, 3)])
    puzzle.add_palindrome([(2, 0), (2, 1), (3, 0), (4, 0), (3, 1)])
    puzzle.add_palindrome([(0, 6), (1, 6), (2, 5)])
    puzzle.add_palindrome([(6, 5), (5, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(2, 7), (3, 7), (4, 6)])

    return puzzle
