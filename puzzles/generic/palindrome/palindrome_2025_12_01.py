"""PuzzleMadness Palindrome Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 6, 0, 0, 0, 0],
        [0, 6, 1, 0, 0, 0, 0, 2, 0],
        [0, 3, 0, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [3, 0, 8, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 6), (4, 5), (4, 6), (5, 5), (6, 5), (7, 4), (7, 3)])
    puzzle.add_palindrome([(7, 5), (8, 4), (8, 5), (7, 6), (6, 6), (5, 6)])
    puzzle.add_palindrome([(0, 1), (1, 0), (2, 0), (3, 1), (3, 2)])
    puzzle.add_palindrome([(0, 8), (1, 7), (2, 6), (3, 5), (3, 4), (3, 3)])
    puzzle.add_palindrome([(5, 8), (5, 7), (6, 7)])
    puzzle.add_palindrome([(5, 1), (5, 2), (6, 3)])
    puzzle.add_palindrome([(5, 0), (6, 1), (7, 1)])

    return puzzle
