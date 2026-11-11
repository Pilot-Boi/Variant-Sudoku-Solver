"""PuzzleMadness Palindrome Sudoku — 2025-06-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 1, 0, 0, 9, 8, 0, 0, 0],
        [0, 2, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 3), (3, 2)])
    puzzle.add_palindrome([(7, 4), (8, 4), (8, 3), (7, 2), (8, 2)])
    puzzle.add_palindrome([(2, 7), (1, 6), (0, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_palindrome([(5, 0), (6, 1), (6, 2)])
    puzzle.add_palindrome([(2, 2), (2, 1), (3, 1)])
    puzzle.add_palindrome([(6, 4), (5, 5), (6, 6), (5, 7)])

    return puzzle
