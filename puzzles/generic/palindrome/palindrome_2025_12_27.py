"""PuzzleMadness Palindrome Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [7, 0, 0, 1, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 4, 0],
        [1, 0, 0, 0, 0, 0, 0, 6, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 4), (6, 3), (6, 2), (5, 3), (4, 2), (3, 1), (2, 1), (1, 1)])
    puzzle.add_palindrome([(3, 3), (3, 2), (2, 2), (1, 3), (0, 4), (0, 5)])
    puzzle.add_palindrome([(1, 4), (2, 4), (1, 5), (1, 6), (0, 7)])
    puzzle.add_palindrome([(7, 4), (8, 4), (7, 3), (7, 2), (6, 1)])
    puzzle.add_palindrome([(4, 8), (5, 7), (6, 6), (7, 6)])
    puzzle.add_palindrome([(1, 7), (2, 7), (3, 6), (2, 5)])

    return puzzle
