"""PuzzleMadness Palindrome Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [5, 6, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 1, 6, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (5, 6), (6, 6), (7, 5), (8, 4), (8, 3), (8, 2)])
    puzzle.add_palindrome([(0, 1), (1, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_palindrome([(3, 2), (3, 3), (2, 4), (3, 5), (2, 5), (1, 6)])
    puzzle.add_palindrome([(5, 1), (6, 2), (5, 3), (6, 4), (7, 3), (7, 4)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 8)])
    puzzle.add_palindrome([(4, 7), (3, 6), (2, 6)])
    puzzle.add_palindrome([(3, 4), (4, 3), (5, 2)])

    return puzzle
