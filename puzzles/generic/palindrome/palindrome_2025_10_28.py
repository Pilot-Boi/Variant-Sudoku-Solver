"""PuzzleMadness Palindrome Sudoku — 2025-10-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [6, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 4, 8],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [2, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (2, 7), (2, 6), (3, 6), (2, 5), (3, 4), (3, 3), (4, 2)])
    puzzle.add_palindrome([(4, 5), (4, 6), (5, 6), (6, 7), (7, 7), (8, 6)])
    puzzle.add_palindrome([(5, 3), (4, 3), (5, 2), (6, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(3, 2), (3, 1), (2, 1), (2, 0), (1, 1)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 3), (7, 2)])
    puzzle.add_palindrome([(7, 4), (6, 5), (7, 6), (6, 6)])
    puzzle.add_palindrome([(1, 2), (0, 3), (0, 4)])

    return puzzle
