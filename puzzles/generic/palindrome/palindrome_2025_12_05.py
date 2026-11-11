"""PuzzleMadness Palindrome Sudoku — 2025-12-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 8, 0, 0],
        [0, 0, 4, 3, 0, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (3, 1), (4, 0), (3, 0), (2, 1), (1, 2), (0, 2), (1, 3)])
    puzzle.add_palindrome([(4, 1), (4, 2), (5, 1), (6, 2), (6, 3), (7, 2)])
    puzzle.add_palindrome([(4, 5), (5, 5), (5, 4), (6, 5), (6, 4), (7, 4)])
    puzzle.add_palindrome([(4, 4), (5, 3), (5, 2)])
    puzzle.add_palindrome([(7, 6), (6, 6), (5, 7), (4, 8)])
    puzzle.add_palindrome([(2, 4), (1, 5), (0, 6)])

    return puzzle
