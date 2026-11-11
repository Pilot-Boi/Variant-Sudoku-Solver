"""PuzzleMadness Palindrome Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 2, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 6, 0, 7, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 5, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 7, 0, 0, 8, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 7), (4, 8), (4, 7), (3, 7), (2, 6), (2, 7), (1, 8)])
    puzzle.add_palindrome([(5, 6), (4, 5), (4, 6), (3, 6), (3, 5)])
    puzzle.add_palindrome([(4, 4), (5, 5), (5, 4), (6, 3), (7, 4), (7, 5)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 3)])
    puzzle.add_palindrome([(6, 0), (5, 0), (4, 1)])
    puzzle.add_palindrome([(8, 7), (7, 6), (6, 5), (6, 4)])

    return puzzle
