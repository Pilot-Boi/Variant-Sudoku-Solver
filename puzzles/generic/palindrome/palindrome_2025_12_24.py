"""PuzzleMadness Palindrome Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [7, 2, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 3, 0, 9],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (8, 5), (7, 4), (6, 3), (6, 2), (5, 1), (5, 2)])
    puzzle.add_palindrome([(2, 5), (3, 6), (2, 7), (1, 7), (1, 6)])
    puzzle.add_palindrome([(5, 7), (5, 6), (4, 5), (3, 5), (4, 4)])
    puzzle.add_palindrome([(2, 3), (3, 2), (4, 2), (5, 3), (6, 4)])
    puzzle.add_palindrome([(8, 6), (7, 6), (6, 5), (5, 5)])
    puzzle.add_palindrome([(1, 4), (1, 3), (0, 2)])
    puzzle.add_palindrome([(0, 7), (0, 6), (1, 5), (2, 4)])

    return puzzle
