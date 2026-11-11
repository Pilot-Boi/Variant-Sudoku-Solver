"""PuzzleMadness Palindrome Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [3, 0, 9, 4, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 4, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 5, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 7), (2, 8), (3, 7), (3, 6), (2, 5), (1, 4), (0, 4), (1, 3)])
    puzzle.add_palindrome([(6, 2), (5, 3), (5, 2), (4, 1), (5, 0)])
    puzzle.add_palindrome([(6, 6), (6, 5), (5, 5), (6, 4), (5, 4), (4, 3)])
    puzzle.add_palindrome([(4, 7), (5, 6), (5, 7), (6, 8), (7, 7), (8, 8)])
    puzzle.add_palindrome([(3, 2), (4, 2), (3, 3), (2, 3)])
    puzzle.add_palindrome([(7, 4), (7, 3), (8, 2)])
    puzzle.add_palindrome([(3, 0), (3, 1), (2, 2)])

    return puzzle
