"""PuzzleMadness Palindrome Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 4, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 6, 5, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 4, 2, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 7],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 2), (7, 1), (6, 2), (5, 2), (4, 3), (5, 3), (6, 4), (6, 5)])
    puzzle.add_palindrome([(4, 2), (3, 2), (2, 1), (3, 0), (2, 0), (1, 1)])
    puzzle.add_palindrome([(3, 6), (4, 5), (4, 6), (5, 5), (5, 6), (6, 7)])
    puzzle.add_palindrome([(7, 4), (8, 4), (7, 5), (6, 6), (7, 7), (8, 6)])
    puzzle.add_palindrome([(2, 3), (3, 4), (3, 5)])
    puzzle.add_palindrome([(6, 0), (5, 1), (4, 1)])

    return puzzle
