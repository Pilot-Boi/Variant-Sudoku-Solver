"""PuzzleMadness Palindrome Sudoku — 2025-04-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 4, 8, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 3, 4],
        [0, 0, 5, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [2, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 7, 0, 2, 1, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 1), (7, 0), (7, 1), (6, 1), (5, 2), (4, 1), (3, 2)])
    puzzle.add_palindrome([(5, 3), (5, 4), (5, 5), (4, 6), (3, 6)])
    puzzle.add_palindrome([(3, 1), (3, 0), (2, 1), (2, 2), (1, 3)])
    puzzle.add_palindrome([(2, 4), (1, 5), (2, 5), (2, 6), (3, 5)])
    puzzle.add_palindrome([(7, 5), (6, 6), (6, 7)])
    puzzle.add_palindrome([(0, 3), (0, 2), (1, 2)])

    return puzzle
