"""PuzzleMadness Palindrome Sudoku — 2025-09-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 5, 4, 8, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (2, 6), (2, 7), (3, 7), (4, 6), (3, 5), (4, 5)])
    puzzle.add_palindrome([(7, 2), (7, 3), (6, 4), (5, 5), (5, 6), (4, 7)])
    puzzle.add_palindrome([(2, 3), (1, 3), (0, 3), (0, 2), (1, 2)])
    puzzle.add_palindrome([(4, 4), (4, 3), (5, 3), (4, 2), (3, 1), (2, 1)])
    puzzle.add_palindrome([(4, 0), (5, 1), (6, 2), (6, 1)])
    puzzle.add_palindrome([(5, 7), (6, 6), (7, 5)])

    return puzzle
