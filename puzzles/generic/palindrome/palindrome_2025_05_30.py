"""PuzzleMadness Palindrome Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 2, 1, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 4, 0, 0],
        [0, 6, 5, 0, 4, 3, 0, 1, 0],
        [2, 4, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2)])
    puzzle.add_palindrome([(7, 0), (6, 1), (5, 0), (4, 0), (5, 1)])
    puzzle.add_palindrome([(4, 7), (5, 7), (5, 6), (6, 7), (6, 6), (6, 5)])
    puzzle.add_palindrome([(4, 6), (3, 7), (2, 8), (2, 7)])
    puzzle.add_palindrome([(6, 4), (5, 4), (4, 5)])

    return puzzle
