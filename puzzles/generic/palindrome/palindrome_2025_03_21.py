"""PuzzleMadness Palindrome Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 8, 2, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 5, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (6, 4), (5, 3), (6, 3), (5, 2), (4, 2), (3, 1), (2, 2)])
    puzzle.add_palindrome([(7, 6), (6, 6), (5, 7), (6, 8), (5, 8), (4, 7)])
    puzzle.add_palindrome([(1, 0), (2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(1, 3), (1, 2), (0, 2)])
    puzzle.add_palindrome([(3, 4), (4, 5), (4, 6)])
    puzzle.add_palindrome([(2, 7), (1, 6), (0, 5), (1, 5)])

    return puzzle
