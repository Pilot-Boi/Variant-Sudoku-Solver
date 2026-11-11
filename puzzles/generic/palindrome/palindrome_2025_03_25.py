"""PuzzleMadness Palindrome Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 8, 0, 9],
        [6, 0, 0, 0, 9, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 6, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 4, 5, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 2), (3, 1), (3, 0), (2, 0), (1, 1), (2, 2), (2, 1)])
    puzzle.add_palindrome([(3, 3), (2, 4), (3, 4), (3, 5), (2, 6)])
    puzzle.add_palindrome([(6, 7), (5, 7), (6, 6), (6, 5), (5, 6)])
    puzzle.add_palindrome([(7, 1), (6, 1), (5, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(5, 2), (4, 3), (4, 4)])
    puzzle.add_palindrome([(7, 6), (8, 6), (8, 5)])
    puzzle.add_palindrome([(1, 7), (2, 8), (3, 7), (3, 6)])

    return puzzle
