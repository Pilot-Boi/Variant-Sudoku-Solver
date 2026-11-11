"""PuzzleMadness Palindrome Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 5, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 3, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 5), (2, 6), (1, 7), (1, 6), (0, 5), (1, 4), (2, 4)])
    puzzle.add_palindrome([(4, 1), (4, 2), (3, 2), (2, 1), (1, 0), (0, 0)])
    puzzle.add_palindrome([(4, 6), (5, 7), (6, 7), (7, 6), (7, 5)])
    puzzle.add_palindrome([(7, 4), (7, 3), (6, 3), (5, 4), (5, 3)])
    puzzle.add_palindrome([(4, 0), (5, 1), (6, 2), (7, 2)])
    puzzle.add_palindrome([(6, 4), (5, 5), (4, 5)])
    puzzle.add_palindrome([(0, 4), (0, 3), (1, 2)])

    return puzzle
