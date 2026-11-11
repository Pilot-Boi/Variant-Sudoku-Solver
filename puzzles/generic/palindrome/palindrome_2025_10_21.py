"""PuzzleMadness Palindrome Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 5, 0, 0, 0, 8, 0],
        [0, 0, 4, 0, 0, 1, 0, 3, 0],
        [1, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [8, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 0), (5, 0), (5, 1), (6, 0), (7, 0), (7, 1), (8, 2)])
    puzzle.add_palindrome([(8, 5), (8, 4), (8, 3), (7, 2), (6, 1), (6, 2)])
    puzzle.add_palindrome([(5, 6), (5, 5), (6, 5), (7, 6), (6, 6), (6, 7)])
    puzzle.add_palindrome([(1, 2), (1, 1), (2, 0), (3, 0), (4, 1)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 6), (1, 7)])
    puzzle.add_palindrome([(5, 4), (6, 4), (7, 5)])
    puzzle.add_palindrome([(4, 5), (3, 4), (2, 4)])

    return puzzle
