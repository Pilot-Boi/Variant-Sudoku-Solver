"""PuzzleMadness Palindrome Sudoku — 2025-04-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 8, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 8, 0, 7, 0, 0, 0, 0],
        [0, 0, 4, 0, 9, 0, 0, 2, 1],
        [0, 3, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 2), (8, 1), (7, 0), (6, 0), (5, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(7, 5), (6, 5), (6, 4), (5, 4), (4, 3)])
    puzzle.add_palindrome([(1, 6), (2, 5), (3, 5), (2, 4), (3, 3), (3, 2)])
    puzzle.add_palindrome([(1, 4), (0, 3), (1, 2), (0, 1)])
    puzzle.add_palindrome([(2, 7), (3, 7), (2, 6), (3, 6)])
    puzzle.add_palindrome([(6, 2), (5, 2), (4, 1)])

    return puzzle
