"""PuzzleMadness Palindrome Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 8, 0, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 6, 0, 0, 8, 2],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (8, 4), (8, 5), (8, 6), (7, 7), (6, 8), (6, 7)])
    puzzle.add_palindrome([(3, 2), (2, 2), (1, 3), (1, 4), (0, 5)])
    puzzle.add_palindrome([(2, 6), (3, 6), (4, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(4, 2), (3, 3), (2, 4), (2, 5), (1, 6)])
    puzzle.add_palindrome([(7, 2), (8, 2), (8, 3)])
    puzzle.add_palindrome([(6, 6), (5, 5), (6, 4), (5, 4)])
    puzzle.add_palindrome([(4, 3), (5, 3), (6, 2), (7, 1)])

    return puzzle
