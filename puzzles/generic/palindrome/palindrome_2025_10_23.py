"""PuzzleMadness Palindrome Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 8],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 1, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 7), (7, 8)])
    puzzle.add_palindrome([(3, 0), (4, 1), (5, 2), (6, 1), (7, 2), (7, 1)])
    puzzle.add_palindrome([(6, 7), (6, 8), (5, 7), (4, 6), (4, 5)])
    puzzle.add_palindrome([(5, 3), (4, 2), (3, 3), (2, 4)])
    puzzle.add_palindrome([(7, 3), (6, 3), (6, 2)])
    puzzle.add_palindrome([(1, 4), (2, 5), (3, 4), (4, 3)])

    return puzzle
