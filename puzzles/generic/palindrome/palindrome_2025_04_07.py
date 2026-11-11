"""PuzzleMadness Palindrome Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 6, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 6, 0, 7],
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 5, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 0), (4, 1), (3, 2), (4, 3), (5, 2), (6, 1), (7, 0), (7, 1)])
    puzzle.add_palindrome([(6, 5), (7, 4), (8, 3), (7, 2), (8, 1), (8, 2)])
    puzzle.add_palindrome([(8, 6), (7, 6), (6, 7), (5, 6), (5, 5), (4, 5)])
    puzzle.add_palindrome([(1, 3), (2, 4), (3, 4)])
    puzzle.add_palindrome([(1, 6), (2, 6), (3, 5)])

    return puzzle
