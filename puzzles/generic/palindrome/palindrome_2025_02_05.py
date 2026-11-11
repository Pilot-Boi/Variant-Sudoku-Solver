"""PuzzleMadness Palindrome Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [3, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 5, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 5), (3, 4), (4, 4), (5, 5), (6, 4), (7, 3), (7, 2), (8, 1)])
    puzzle.add_palindrome([(2, 3), (1, 4), (0, 5), (0, 6), (1, 6)])
    puzzle.add_palindrome([(1, 2), (2, 1), (2, 2), (3, 1), (4, 0), (4, 1)])
    puzzle.add_palindrome([(6, 2), (5, 3), (4, 2), (3, 3)])
    puzzle.add_palindrome([(7, 7), (8, 6), (8, 5)])
    puzzle.add_palindrome([(7, 5), (6, 6), (6, 7)])

    return puzzle
