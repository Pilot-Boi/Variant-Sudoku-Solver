"""PuzzleMadness Palindrome Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 9, 0, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 6, 5, 0, 0, 7, 0],
        [0, 0, 0, 3, 0, 1, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1), (6, 2), (6, 3)])
    puzzle.add_palindrome([(8, 7), (8, 6), (8, 5), (7, 5), (6, 5)])
    puzzle.add_palindrome([(5, 1), (5, 2), (4, 3), (4, 4), (3, 5)])
    puzzle.add_palindrome([(2, 3), (3, 2), (2, 1), (1, 0), (0, 1)])
    puzzle.add_palindrome([(7, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(5, 3), (6, 4), (7, 4)])
    puzzle.add_palindrome([(3, 8), (2, 7), (1, 7)])

    return puzzle
