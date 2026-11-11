"""PuzzleMadness Palindrome Sudoku — 2025-03-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [0, 0, 0, 4, 0, 0, 8, 1, 0],
        [6, 0, 1, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [2, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 5), (4, 5), (3, 5), (2, 4), (3, 3), (2, 3), (2, 2), (3, 1)])
    puzzle.add_palindrome([(2, 5), (1, 4), (1, 5), (2, 6), (3, 6), (4, 7)])
    puzzle.add_palindrome([(5, 3), (6, 2), (6, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_palindrome([(6, 4), (5, 4), (4, 3), (3, 2), (4, 2), (5, 2)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 8)])
    puzzle.add_palindrome([(1, 2), (0, 2), (0, 3)])
    puzzle.add_palindrome([(6, 3), (7, 3), (8, 2)])

    return puzzle
