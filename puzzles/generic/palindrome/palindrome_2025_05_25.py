"""PuzzleMadness Palindrome Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 9, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 8, 3, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 7), (6, 6), (7, 7), (8, 6), (7, 5), (8, 5), (7, 4), (8, 4)])
    puzzle.add_palindrome([(7, 3), (6, 4), (6, 5), (5, 5), (4, 6)])
    puzzle.add_palindrome([(4, 1), (3, 2), (3, 3), (4, 3), (3, 4)])
    puzzle.add_palindrome([(5, 2), (5, 1), (4, 2), (5, 3), (4, 4), (3, 5)])
    puzzle.add_palindrome([(1, 7), (1, 6), (2, 5)])
    puzzle.add_palindrome([(1, 3), (0, 3), (0, 2)])
    puzzle.add_palindrome([(0, 1), (1, 2), (2, 3)])

    return puzzle
