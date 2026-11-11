"""PuzzleMadness Palindrome Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 1, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 3, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 8, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 4), (4, 3), (5, 3), (5, 2), (4, 2), (3, 2), (2, 3)])
    puzzle.add_palindrome([(7, 5), (8, 4), (8, 5), (7, 6), (6, 6), (6, 7)])
    puzzle.add_palindrome([(0, 6), (1, 7), (2, 8), (3, 8), (3, 7)])
    puzzle.add_palindrome([(4, 1), (4, 0), (5, 0), (6, 1), (7, 0)])
    puzzle.add_palindrome([(2, 7), (3, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(6, 3), (6, 2), (7, 2)])

    return puzzle
