"""PuzzleMadness Palindrome Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 8, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 9],
        [0, 7, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 6), (3, 5), (3, 4), (4, 3), (5, 2), (4, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(2, 4), (3, 3), (3, 2), (2, 1), (2, 0), (3, 0)])
    puzzle.add_palindrome([(5, 6), (4, 6), (3, 7), (2, 8), (1, 8), (1, 7)])
    puzzle.add_palindrome([(6, 1), (5, 1), (6, 2), (7, 3)])
    puzzle.add_palindrome([(7, 6), (6, 6), (5, 7)])
    puzzle.add_palindrome([(2, 3), (1, 2), (0, 2)])

    return puzzle
