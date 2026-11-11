"""PuzzleMadness Palindrome Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 7, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 7, 4, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 3), (6, 4), (5, 5), (4, 6), (3, 7), (3, 6), (2, 7)])
    puzzle.add_palindrome([(3, 5), (4, 5), (3, 4), (2, 3), (2, 4), (1, 3)])
    puzzle.add_palindrome([(4, 8), (5, 7), (6, 6), (7, 5), (8, 5)])
    puzzle.add_palindrome([(6, 2), (7, 3), (8, 2), (8, 3)])
    puzzle.add_palindrome([(2, 6), (1, 6), (0, 5), (0, 4)])
    puzzle.add_palindrome([(2, 2), (1, 2), (0, 3)])

    return puzzle
