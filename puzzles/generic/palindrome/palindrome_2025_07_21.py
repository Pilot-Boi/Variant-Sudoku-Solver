"""PuzzleMadness Palindrome Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 7, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 0, 0, 0, 0],
        [6, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [8, 7, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 7), (2, 6), (3, 5), (2, 4), (2, 3), (1, 4), (1, 5)])
    puzzle.add_palindrome([(4, 2), (4, 1), (5, 2), (6, 3), (5, 3), (5, 4)])
    puzzle.add_palindrome([(6, 7), (5, 7), (5, 6), (6, 5), (7, 5)])
    puzzle.add_palindrome([(6, 0), (6, 1), (7, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(7, 4), (7, 3), (6, 2)])
    puzzle.add_palindrome([(6, 4), (5, 5), (4, 6)])

    return puzzle
