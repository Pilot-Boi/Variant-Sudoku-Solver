"""PuzzleMadness Palindrome Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [7, 0, 0, 0, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 1), (7, 2), (6, 3), (5, 3), (6, 4), (5, 5), (4, 6), (4, 5)])
    puzzle.add_palindrome([(2, 5), (2, 6), (2, 7), (3, 8), (3, 7), (4, 7)])
    puzzle.add_palindrome([(1, 5), (2, 4), (2, 3), (1, 2), (2, 1)])
    puzzle.add_palindrome([(5, 7), (5, 6), (6, 6)])
    puzzle.add_palindrome([(4, 8), (5, 8), (6, 7), (7, 6)])
    puzzle.add_palindrome([(6, 2), (6, 1), (5, 0), (4, 1)])

    return puzzle
