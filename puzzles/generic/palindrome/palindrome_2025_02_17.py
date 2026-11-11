"""PuzzleMadness Palindrome Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 9, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 4, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 2, 0, 0, 0],
        [0, 6, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 7), (4, 8), (5, 7), (6, 6), (6, 5), (7, 4), (8, 3)])
    puzzle.add_palindrome([(4, 1), (5, 2), (6, 2), (6, 1), (7, 2)])
    puzzle.add_palindrome([(5, 6), (4, 6), (3, 5), (2, 6), (1, 7), (2, 7)])
    puzzle.add_palindrome([(5, 3), (4, 2), (3, 1), (2, 1), (3, 0)])
    puzzle.add_palindrome([(6, 7), (7, 6), (8, 5)])
    puzzle.add_palindrome([(3, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(4, 5), (5, 5), (6, 4), (7, 3)])

    return puzzle
