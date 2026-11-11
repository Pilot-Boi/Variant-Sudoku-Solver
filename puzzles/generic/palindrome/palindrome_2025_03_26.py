"""PuzzleMadness Palindrome Sudoku — 2025-03-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 6, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 4, 0, 7],
        [0, 7, 0, 0, 1, 0, 2, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 2), (5, 1), (6, 2), (5, 2), (5, 3), (6, 3), (6, 4)])
    puzzle.add_palindrome([(2, 5), (1, 4), (0, 3), (1, 2), (0, 1), (0, 2)])
    puzzle.add_palindrome([(6, 7), (6, 8), (5, 7), (5, 6), (4, 5)])
    puzzle.add_palindrome([(1, 1), (2, 2), (2, 1), (3, 0), (4, 1), (3, 2)])
    puzzle.add_palindrome([(5, 4), (6, 5), (7, 6)])
    puzzle.add_palindrome([(7, 1), (6, 0), (5, 0)])
    puzzle.add_palindrome([(3, 8), (2, 8), (2, 7)])

    return puzzle
