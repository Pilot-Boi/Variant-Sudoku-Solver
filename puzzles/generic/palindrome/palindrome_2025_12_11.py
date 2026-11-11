"""PuzzleMadness Palindrome Sudoku — 2025-12-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 1, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 8, 0, 0, 5],
        [0, 0, 0, 0, 0, 1, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (2, 6), (2, 7), (3, 7), (4, 8), (5, 7), (4, 6)])
    puzzle.add_palindrome([(2, 3), (3, 3), (4, 3), (4, 2), (5, 2)])
    puzzle.add_palindrome([(5, 6), (5, 5), (6, 5), (7, 6), (8, 5)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 4), (5, 3), (6, 2), (6, 1)])
    puzzle.add_palindrome([(0, 3), (1, 3), (0, 2), (1, 1)])
    puzzle.add_palindrome([(2, 0), (2, 1), (3, 0), (4, 1)])

    return puzzle
