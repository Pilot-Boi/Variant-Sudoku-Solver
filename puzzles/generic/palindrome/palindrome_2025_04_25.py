"""PuzzleMadness Palindrome Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 9, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 5, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (8, 4), (7, 3), (6, 2), (6, 1), (5, 1), (4, 2)])
    puzzle.add_palindrome([(3, 8), (4, 8), (3, 7), (2, 8), (1, 7), (0, 7)])
    puzzle.add_palindrome([(3, 3), (2, 3), (1, 3), (0, 2), (1, 1)])
    puzzle.add_palindrome([(8, 5), (7, 6), (6, 5), (5, 5), (5, 6)])
    puzzle.add_palindrome([(7, 1), (6, 0), (5, 0)])
    puzzle.add_palindrome([(0, 4), (0, 5), (1, 6), (2, 6)])
    puzzle.add_palindrome([(4, 7), (3, 6), (2, 5), (3, 4)])

    return puzzle
