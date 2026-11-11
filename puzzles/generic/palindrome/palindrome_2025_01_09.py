"""PuzzleMadness Palindrome Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 6, 3, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 7, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 1), (5, 2), (5, 3), (6, 2), (7, 1), (7, 0), (8, 0)])
    puzzle.add_palindrome([(5, 5), (5, 4), (6, 3), (7, 3), (6, 4)])
    puzzle.add_palindrome([(4, 8), (5, 7), (5, 6), (6, 7), (7, 8), (8, 7)])
    puzzle.add_palindrome([(1, 2), (2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_palindrome([(5, 0), (6, 0), (6, 1)])
    puzzle.add_palindrome([(3, 4), (2, 3), (3, 2), (4, 2)])

    return puzzle
