"""PuzzleMadness Palindrome Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 8, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 2, 0, 0, 0],
        [0, 0, 5, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 6, 0, 3],
        [0, 7, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 7), (8, 8), (7, 8), (6, 7), (5, 6), (4, 6), (3, 6), (2, 6)])
    puzzle.add_palindrome([(3, 4), (3, 3), (2, 3), (2, 4), (1, 5)])
    puzzle.add_palindrome([(4, 4), (5, 4), (4, 3), (3, 2), (4, 2), (3, 1)])
    puzzle.add_palindrome([(8, 7), (8, 6), (7, 5), (6, 5)])
    puzzle.add_palindrome([(6, 3), (6, 2), (5, 2)])

    return puzzle
