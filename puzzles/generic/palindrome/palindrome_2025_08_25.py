"""PuzzleMadness Palindrome Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 6],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [4, 6, 0, 0, 0, 0, 1, 0, 8],
        [0, 7, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (3, 3), (2, 2), (2, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_palindrome([(6, 1), (7, 1), (8, 2), (8, 3), (7, 4)])
    puzzle.add_palindrome([(4, 7), (5, 7), (4, 6), (3, 5), (2, 6)])
    puzzle.add_palindrome([(3, 8), (3, 7), (2, 7), (2, 8), (1, 7)])
    puzzle.add_palindrome([(7, 5), (6, 5), (5, 6), (6, 7)])
    puzzle.add_palindrome([(0, 3), (1, 2), (1, 1)])
    puzzle.add_palindrome([(3, 1), (3, 0), (2, 0)])

    return puzzle
