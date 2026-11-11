"""PuzzleMadness Palindrome Sudoku — 2025-03-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 7, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 9, 0, 0, 2, 0],
        [2, 0, 0, 0, 0, 0, 3, 0, 4],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 7), (6, 8), (6, 7), (7, 6), (8, 5), (8, 4), (7, 5), (6, 5)])
    puzzle.add_palindrome([(4, 5), (4, 4), (3, 3), (4, 2), (5, 1), (5, 2)])
    puzzle.add_palindrome([(2, 3), (2, 4), (1, 5), (0, 6), (1, 6), (0, 7)])
    puzzle.add_palindrome([(5, 3), (6, 3), (5, 4), (5, 5), (4, 6)])
    puzzle.add_palindrome([(2, 5), (3, 5), (3, 6)])
    puzzle.add_palindrome([(1, 3), (1, 2), (0, 1)])

    return puzzle
