"""PuzzleMadness Palindrome Sudoku — 2025-09-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-09-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/9/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 8, 1, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 8, 0, 0],
        [3, 0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 6), (5, 6), (6, 5), (7, 6), (8, 6), (7, 7), (6, 7)])
    puzzle.add_palindrome([(6, 2), (6, 1), (6, 0), (5, 1), (4, 0), (4, 1)])
    puzzle.add_palindrome([(0, 1), (1, 0), (2, 0), (3, 1), (3, 2)])
    puzzle.add_palindrome([(0, 7), (1, 6), (0, 5), (1, 5)])
    puzzle.add_palindrome([(3, 8), (3, 7), (2, 6), (2, 5)])
    puzzle.add_palindrome([(3, 4), (4, 3), (5, 2), (4, 2)])

    return puzzle
