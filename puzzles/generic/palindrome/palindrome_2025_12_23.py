"""PuzzleMadness Palindrome Sudoku — 2025-12-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 5, 6, 0],
        [0, 0, 1, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (4, 5), (5, 4), (6, 4), (7, 3), (7, 4), (8, 4)])
    puzzle.add_palindrome([(2, 2), (2, 3), (3, 2), (4, 2), (3, 1)])
    puzzle.add_palindrome([(4, 8), (5, 7), (5, 8), (6, 7), (7, 6), (7, 5)])
    puzzle.add_palindrome([(6, 3), (6, 2), (6, 1), (5, 1), (4, 1)])
    puzzle.add_palindrome([(4, 3), (3, 4), (2, 5), (1, 4)])
    puzzle.add_palindrome([(3, 6), (3, 5), (4, 4)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 5), (0, 4)])

    return puzzle
