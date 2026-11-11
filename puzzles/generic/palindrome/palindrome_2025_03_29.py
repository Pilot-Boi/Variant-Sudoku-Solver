"""PuzzleMadness Palindrome Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 1, 0, 9],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 8, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 9, 7, 2],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 4), (7, 4), (8, 5), (7, 6), (8, 7), (7, 8), (6, 8)])
    puzzle.add_palindrome([(3, 6), (3, 5), (2, 4), (1, 4), (0, 4)])
    puzzle.add_palindrome([(4, 7), (4, 8), (5, 7), (6, 6), (6, 5), (5, 4)])
    puzzle.add_palindrome([(2, 1), (3, 1), (2, 2), (1, 2), (0, 3)])
    puzzle.add_palindrome([(5, 1), (5, 2), (6, 3), (6, 2)])
    puzzle.add_palindrome([(3, 7), (2, 6), (1, 6)])

    return puzzle
