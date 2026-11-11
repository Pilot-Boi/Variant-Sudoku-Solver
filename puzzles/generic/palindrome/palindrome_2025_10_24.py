"""PuzzleMadness Palindrome Sudoku — 2025-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [7, 0, 0, 9, 0, 0, 0, 6, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 3, 0, 2, 0, 4, 0, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 3, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 4), (7, 4), (6, 3), (7, 2), (8, 2), (8, 1), (8, 0)])
    puzzle.add_palindrome([(6, 7), (7, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_palindrome([(3, 6), (3, 7), (4, 6), (4, 5), (5, 5)])
    puzzle.add_palindrome([(0, 8), (0, 7), (0, 6), (1, 5), (2, 5), (1, 4)])
    puzzle.add_palindrome([(3, 3), (3, 2), (4, 3), (5, 2)])
    puzzle.add_palindrome([(6, 0), (5, 0), (4, 1)])

    return puzzle
