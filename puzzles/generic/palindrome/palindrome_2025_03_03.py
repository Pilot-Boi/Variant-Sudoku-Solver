"""PuzzleMadness Palindrome Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 1, 0],
        [0, 0, 0, 0, 8, 7, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 6), (6, 7), (7, 7), (7, 6), (6, 5), (5, 6), (4, 7)])
    puzzle.add_palindrome([(4, 2), (5, 2), (6, 3), (5, 4), (6, 4), (7, 5)])
    puzzle.add_palindrome([(2, 8), (2, 7), (3, 6), (4, 5), (3, 5)])
    puzzle.add_palindrome([(1, 1), (0, 2), (1, 2), (2, 3), (1, 3), (0, 4)])
    puzzle.add_palindrome([(6, 2), (6, 1), (5, 0), (5, 1)])
    puzzle.add_palindrome([(2, 4), (3, 4), (4, 3)])
    puzzle.add_palindrome([(1, 0), (2, 0), (3, 1)])

    return puzzle
