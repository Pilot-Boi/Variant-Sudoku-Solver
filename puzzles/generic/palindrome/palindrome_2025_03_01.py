"""PuzzleMadness Palindrome Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 7],
        [0, 0, 0, 5, 0, 0, 0, 8, 3],
        [0, 0, 0, 0, 7, 6, 0, 1, 0],
        [0, 0, 6, 0, 0, 5, 0, 0, 2],
        [0, 2, 0, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 9, 0],
        [4, 5, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 6), (7, 5), (6, 6), (5, 6), (4, 5), (5, 5), (4, 4), (3, 5)])
    puzzle.add_palindrome([(6, 1), (7, 1), (7, 2), (6, 3), (5, 2)])
    puzzle.add_palindrome([(4, 6), (5, 7), (6, 8), (7, 8), (8, 8)])
    puzzle.add_palindrome([(2, 2), (1, 2), (0, 3)])
    puzzle.add_palindrome([(2, 0), (3, 1), (4, 1)])

    return puzzle
