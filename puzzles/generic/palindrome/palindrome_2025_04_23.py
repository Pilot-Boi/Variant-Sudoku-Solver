"""PuzzleMadness Palindrome Sudoku — 2025-04-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 5, 0, 0],
        [7, 0, 0, 0, 6, 0, 2, 0, 8],
        [0, 0, 6, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 4), (5, 4), (6, 5), (6, 4), (5, 3), (6, 3), (7, 3)])
    puzzle.add_palindrome([(6, 7), (6, 6), (7, 6), (7, 5), (8, 5)])
    puzzle.add_palindrome([(4, 2), (5, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (2, 5)])
    puzzle.add_palindrome([(3, 8), (2, 7), (2, 6)])

    return puzzle
