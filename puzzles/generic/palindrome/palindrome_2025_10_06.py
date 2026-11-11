"""PuzzleMadness Palindrome Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 3, 7],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 0), (8, 1), (7, 2), (7, 3), (6, 2), (5, 3), (5, 2), (4, 2)])
    puzzle.add_palindrome([(4, 7), (3, 6), (4, 6), (5, 5), (6, 6)])
    puzzle.add_palindrome([(2, 8), (3, 8), (3, 7), (2, 6), (2, 5), (1, 5)])
    puzzle.add_palindrome([(2, 4), (3, 4), (2, 3), (1, 2), (0, 3), (0, 2)])
    puzzle.add_palindrome([(6, 0), (5, 0), (6, 1), (5, 1)])
    puzzle.add_palindrome([(4, 4), (3, 3), (2, 2), (3, 2)])

    return puzzle
