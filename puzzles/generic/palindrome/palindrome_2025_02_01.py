"""PuzzleMadness Palindrome Sudoku — 2025-02-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 4, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [7, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (7, 5), (7, 4), (6, 3), (5, 4), (4, 3), (3, 2), (4, 2)])
    puzzle.add_palindrome([(5, 0), (4, 0), (5, 1), (6, 2), (6, 1), (7, 1)])
    puzzle.add_palindrome([(3, 6), (2, 5), (2, 6), (1, 5), (0, 6), (0, 5)])
    puzzle.add_palindrome([(5, 6), (5, 7), (6, 8), (7, 8), (7, 7)])
    puzzle.add_palindrome([(2, 2), (2, 3), (3, 4)])
    puzzle.add_palindrome([(1, 2), (1, 3), (2, 4)])

    return puzzle
