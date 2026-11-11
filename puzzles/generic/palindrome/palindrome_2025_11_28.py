"""PuzzleMadness Palindrome Sudoku — 2025-11-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 5, 0, 0, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 0), (6, 1), (7, 1), (6, 2), (5, 3), (5, 2), (4, 2), (4, 1)])
    puzzle.add_palindrome([(2, 3), (1, 4), (2, 5), (3, 5), (4, 6)])
    puzzle.add_palindrome([(7, 2), (6, 3), (6, 4), (5, 5), (4, 5), (4, 4)])
    puzzle.add_palindrome([(3, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
    puzzle.add_palindrome([(5, 6), (6, 6), (7, 7)])
    puzzle.add_palindrome([(3, 6), (2, 6), (1, 7)])

    return puzzle
