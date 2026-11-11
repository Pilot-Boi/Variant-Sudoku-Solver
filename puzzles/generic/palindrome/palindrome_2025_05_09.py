"""PuzzleMadness Palindrome Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [8, 7, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 5, 0, 6, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 0), (7, 0), (6, 0), (5, 0), (4, 1), (5, 2), (4, 2)])
    puzzle.add_palindrome([(7, 6), (7, 7), (6, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_palindrome([(3, 6), (2, 7), (3, 7), (4, 6), (5, 5)])
    puzzle.add_palindrome([(3, 2), (3, 1), (3, 0), (2, 1), (1, 0), (2, 0)])
    puzzle.add_palindrome([(4, 4), (5, 4), (6, 3)])
    puzzle.add_palindrome([(0, 5), (1, 6), (2, 6)])

    return puzzle
