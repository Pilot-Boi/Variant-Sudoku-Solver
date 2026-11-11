"""PuzzleMadness Palindrome Sudoku — 2025-12-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 9, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 8, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (2, 4), (3, 3), (4, 2), (5, 2), (4, 1), (3, 1)])
    puzzle.add_palindrome([(8, 4), (8, 3), (8, 2), (7, 1), (7, 2)])
    puzzle.add_palindrome([(3, 5), (2, 6), (1, 6), (1, 5), (0, 4)])
    puzzle.add_palindrome([(6, 6), (7, 5), (6, 5), (5, 6), (5, 5)])
    puzzle.add_palindrome([(6, 2), (6, 3), (7, 3)])
    puzzle.add_palindrome([(7, 4), (8, 5), (7, 6), (8, 6)])
    puzzle.add_palindrome([(2, 2), (1, 2), (1, 3)])

    return puzzle
