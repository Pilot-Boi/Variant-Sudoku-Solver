"""PuzzleMadness Palindrome Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 9, 3, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 7, 0, 1, 0, 0],
        [0, 0, 0, 3, 0, 0, 9, 0, 8],
        [2, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(2, 1), (3, 0), (4, 1), (5, 0), (6, 1), (7, 2), (6, 3), (5, 2)])
    puzzle.add_palindrome([(0, 3), (0, 4), (0, 5), (1, 6), (1, 7), (1, 8)])
    puzzle.add_palindrome([(4, 6), (5, 7), (5, 6), (6, 5), (7, 6), (6, 7)])
    puzzle.add_palindrome([(4, 5), (3, 4), (2, 3)])
    puzzle.add_palindrome([(3, 2), (2, 2), (1, 1)])
    puzzle.add_palindrome([(6, 4), (5, 4), (5, 3)])

    return puzzle
