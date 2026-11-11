"""PuzzleMadness Palindrome Sudoku — 2025-02-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 2, 7, 0, 0, 9, 0, 0, 8],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 4), (6, 5), (7, 4), (7, 3), (6, 2), (5, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(1, 4), (0, 4), (1, 5), (1, 6), (2, 7)])
    puzzle.add_palindrome([(4, 6), (3, 6), (2, 6), (3, 5), (4, 4), (3, 3)])
    puzzle.add_palindrome([(7, 5), (8, 5), (8, 6)])
    puzzle.add_palindrome([(3, 0), (3, 1), (2, 0), (1, 1)])
    puzzle.add_palindrome([(5, 3), (5, 2), (4, 2)])

    return puzzle
