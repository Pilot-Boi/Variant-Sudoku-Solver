"""PuzzleMadness Palindrome Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 0, 9, 4],
        [0, 3, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (3, 1), (4, 2), (5, 3), (6, 3), (5, 4), (6, 5)])
    puzzle.add_palindrome([(7, 6), (7, 7), (6, 7), (5, 8), (4, 8), (5, 7)])
    puzzle.add_palindrome([(6, 2), (6, 1), (7, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(2, 8), (3, 7), (3, 6), (4, 5), (5, 5), (5, 6)])
    puzzle.add_palindrome([(0, 2), (1, 3), (2, 3)])
    puzzle.add_palindrome([(2, 4), (2, 5), (3, 4), (3, 3)])
    puzzle.add_palindrome([(8, 6), (7, 5), (6, 4)])

    return puzzle
