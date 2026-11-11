"""PuzzleMadness Palindrome Sudoku — 2025-10-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 8, 0, 1],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [1, 7, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 1, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 4, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 5), (1, 6), (1, 7), (2, 7), (3, 6), (2, 5), (3, 5), (4, 4)])
    puzzle.add_palindrome([(7, 6), (6, 7), (5, 7), (4, 8), (4, 7)])
    puzzle.add_palindrome([(8, 1), (8, 2), (8, 3), (7, 3), (7, 4)])
    puzzle.add_palindrome([(5, 3), (6, 4), (7, 5), (8, 6), (8, 7), (7, 8)])
    puzzle.add_palindrome([(3, 2), (3, 3), (4, 3)])
    puzzle.add_palindrome([(3, 4), (2, 3), (1, 2)])
    puzzle.add_palindrome([(4, 1), (5, 1), (6, 2)])

    return puzzle
