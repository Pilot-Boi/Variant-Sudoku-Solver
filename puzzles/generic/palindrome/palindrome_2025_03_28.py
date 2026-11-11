"""PuzzleMadness Palindrome Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 4, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 1, 8, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 5, 2, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 7, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 0), (6, 1), (6, 2), (5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(2, 0), (3, 0), (2, 1), (2, 2), (3, 2)])
    puzzle.add_palindrome([(2, 7), (1, 6), (1, 5), (2, 5), (1, 4)])
    puzzle.add_palindrome([(3, 6), (4, 7), (3, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(1, 3), (2, 3), (3, 4), (4, 5)])
    puzzle.add_palindrome([(7, 4), (6, 3), (7, 2), (8, 1)])

    return puzzle
