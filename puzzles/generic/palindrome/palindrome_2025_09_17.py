"""PuzzleMadness Palindrome Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 6, 0],
        [0, 0, 9, 0, 6, 1, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 4, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (1, 7), (1, 6), (2, 5), (3, 4), (2, 4), (3, 3), (2, 2)])
    puzzle.add_palindrome([(7, 4), (8, 3), (7, 3), (8, 2), (7, 1), (8, 0)])
    puzzle.add_palindrome([(5, 0), (6, 1), (5, 1), (4, 2), (4, 3)])
    puzzle.add_palindrome([(6, 5), (5, 4), (6, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_palindrome([(2, 1), (3, 1), (4, 0)])
    puzzle.add_palindrome([(3, 7), (2, 7), (1, 8)])

    return puzzle
