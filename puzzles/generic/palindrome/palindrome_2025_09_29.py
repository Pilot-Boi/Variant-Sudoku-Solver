"""PuzzleMadness Palindrome Sudoku — 2025-09-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 2, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 4],
        [0, 0, 8, 0, 5, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 8), (7, 7), (6, 6), (6, 5), (5, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_palindrome([(0, 2), (1, 1), (1, 2), (2, 3), (2, 4), (1, 4)])
    puzzle.add_palindrome([(1, 5), (0, 6), (1, 6), (2, 5), (3, 6)])
    puzzle.add_palindrome([(5, 4), (6, 4), (7, 5)])
    puzzle.add_palindrome([(4, 3), (5, 3), (4, 2), (5, 1)])

    return puzzle
