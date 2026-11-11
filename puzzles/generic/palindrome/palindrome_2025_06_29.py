"""PuzzleMadness Palindrome Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 8, 0, 0, 0, 0, 0],
        [4, 0, 0, 1, 0, 0, 0, 5, 2],
        [0, 0, 1, 7, 0, 0, 5, 0, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 7), (1, 6), (0, 6), (0, 5), (1, 4), (2, 4), (3, 4)])
    puzzle.add_palindrome([(7, 5), (6, 5), (7, 6), (8, 7), (8, 8)])
    puzzle.add_palindrome([(6, 4), (6, 3), (7, 2), (8, 2), (7, 1)])
    puzzle.add_palindrome([(3, 3), (2, 3), (1, 2), (0, 2), (0, 1)])
    puzzle.add_palindrome([(7, 0), (6, 1), (5, 2), (5, 1)])
    puzzle.add_palindrome([(2, 1), (2, 2), (3, 2)])

    return puzzle
