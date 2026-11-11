"""PuzzleMadness Palindrome Sudoku — 2025-03-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 1, 2, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [2, 0, 4, 0, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 8, 7, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(5, 0), (6, 1), (5, 2), (6, 3), (7, 2), (7, 3), (8, 3), (8, 2)])
    puzzle.add_palindrome([(4, 5), (3, 4), (4, 3), (3, 2), (4, 1), (3, 1)])
    puzzle.add_palindrome([(2, 3), (3, 3), (2, 2), (1, 1), (0, 1)])
    puzzle.add_palindrome([(5, 5), (6, 6), (6, 7)])
    puzzle.add_palindrome([(7, 6), (7, 5), (8, 5)])

    return puzzle
