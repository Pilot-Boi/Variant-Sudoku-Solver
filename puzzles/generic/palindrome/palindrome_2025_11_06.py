"""PuzzleMadness Palindrome Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 4, 0, 6, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 2, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 4, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 7), (5, 7), (4, 8), (5, 8), (6, 7), (7, 6), (8, 6), (7, 5)])
    puzzle.add_palindrome([(3, 1), (3, 2), (4, 3), (5, 4), (4, 4)])
    puzzle.add_palindrome([(4, 0), (3, 0), (2, 0), (2, 1), (2, 2)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 3), (5, 2)])
    puzzle.add_palindrome([(8, 3), (8, 2), (7, 3), (6, 2)])

    return puzzle
