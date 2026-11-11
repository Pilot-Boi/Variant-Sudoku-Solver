"""PuzzleMadness Palindrome Sudoku — 2025-09-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 5, 6, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 0, 5, 4, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 5, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (5, 4), (4, 5), (4, 6), (5, 6), (4, 7), (3, 8)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 7), (7, 7), (8, 8)])
    puzzle.add_palindrome([(7, 5), (8, 4), (7, 3), (7, 2), (6, 1)])
    puzzle.add_palindrome([(2, 0), (1, 1), (2, 2), (3, 1), (3, 2), (4, 2)])
    puzzle.add_palindrome([(6, 6), (7, 6), (6, 5), (5, 5)])
    puzzle.add_palindrome([(2, 6), (2, 5), (1, 4)])
    puzzle.add_palindrome([(3, 6), (2, 7), (1, 7)])

    return puzzle
