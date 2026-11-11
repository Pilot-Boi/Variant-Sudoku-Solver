"""PuzzleMadness Palindrome Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 0, 0, 0, 8, 0, 0, 0],
        [0, 4, 1, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 9, 0, 0, 0],
        [0, 6, 0, 2, 8, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 3), (1, 3), (0, 4), (1, 5), (1, 6), (0, 6), (1, 7)])
    puzzle.add_palindrome([(5, 1), (4, 0), (5, 0), (6, 1), (7, 2), (8, 3)])
    puzzle.add_palindrome([(6, 6), (6, 7), (7, 6), (8, 5), (7, 4)])
    puzzle.add_palindrome([(3, 3), (4, 4), (3, 5), (4, 6), (5, 7), (5, 8)])
    puzzle.add_palindrome([(5, 2), (6, 3), (6, 4)])
    puzzle.add_palindrome([(4, 3), (4, 2), (3, 1)])

    return puzzle
