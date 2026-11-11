"""PuzzleMadness Palindrome Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 1, 0, 0, 6, 0, 0, 0],
        [7, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 8, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (3, 5), (3, 6), (2, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_palindrome([(4, 4), (3, 3), (4, 3), (5, 2), (5, 1), (6, 0)])
    puzzle.add_palindrome([(7, 3), (6, 4), (5, 4), (4, 5), (4, 6)])
    puzzle.add_palindrome([(3, 1), (3, 2), (2, 3), (1, 2)])
    puzzle.add_palindrome([(5, 8), (5, 7), (6, 6)])
    puzzle.add_palindrome([(7, 4), (8, 3), (7, 2), (8, 1)])

    return puzzle
