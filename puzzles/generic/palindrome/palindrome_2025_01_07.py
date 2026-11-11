"""PuzzleMadness Palindrome Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 8, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 6, 0, 7, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 3, 0, 9, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 0), (3, 1), (3, 2), (4, 3), (4, 4), (5, 5), (5, 4)])
    puzzle.add_palindrome([(7, 3), (6, 3), (6, 2), (7, 1), (6, 0)])
    puzzle.add_palindrome([(2, 8), (2, 7), (2, 6), (3, 7), (4, 6), (3, 5)])
    puzzle.add_palindrome([(7, 5), (6, 5), (7, 6), (8, 7)])
    puzzle.add_palindrome([(5, 6), (6, 7), (7, 7)])

    return puzzle
