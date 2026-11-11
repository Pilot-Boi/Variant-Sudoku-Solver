"""PuzzleMadness Palindrome Sudoku — 2025-02-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 2, 0, 0, 0, 3, 0, 0],
        [0, 8, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 9, 6, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 4), (6, 5), (5, 4), (4, 4), (3, 3), (2, 2)])
    puzzle.add_palindrome([(1, 4), (0, 4), (1, 3), (1, 2), (2, 1)])
    puzzle.add_palindrome([(4, 6), (5, 7), (5, 8), (6, 7), (7, 8), (7, 7)])
    puzzle.add_palindrome([(6, 3), (6, 2), (7, 2)])
    puzzle.add_palindrome([(3, 6), (3, 7), (2, 8), (2, 7)])

    return puzzle
