"""PuzzleMadness Palindrome Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 9, 0, 1, 4, 0, 0, 0],
        [0, 8, 4, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 4), (7, 3), (7, 2), (8, 2), (7, 1), (6, 2)])
    puzzle.add_palindrome([(5, 5), (6, 5), (5, 6), (4, 7), (3, 7)])
    puzzle.add_palindrome([(1, 8), (2, 7), (3, 6), (4, 5), (4, 6)])
    puzzle.add_palindrome([(2, 4), (1, 3), (1, 2), (0, 2), (1, 1)])
    puzzle.add_palindrome([(0, 5), (0, 6), (1, 7)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 1), (3, 0)])
    puzzle.add_palindrome([(3, 4), (3, 5), (2, 5)])

    return puzzle
