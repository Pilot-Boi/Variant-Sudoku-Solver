"""PuzzleMadness Palindrome Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 3, 0, 9],
        [6, 0, 0, 0, 2, 0, 0, 1, 0],
        [0, 0, 3, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 7), (6, 6), (5, 6), (4, 5), (3, 5), (2, 4), (1, 5)])
    puzzle.add_palindrome([(3, 0), (3, 1), (3, 2), (4, 3), (5, 3)])
    puzzle.add_palindrome([(8, 0), (7, 1), (6, 0), (5, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(3, 3), (4, 4), (5, 5), (6, 4), (7, 5), (7, 4)])
    puzzle.add_palindrome([(0, 5), (1, 6), (1, 7)])
    puzzle.add_palindrome([(3, 6), (3, 7), (2, 8), (2, 7)])
    puzzle.add_palindrome([(6, 1), (7, 2), (7, 3)])

    return puzzle
