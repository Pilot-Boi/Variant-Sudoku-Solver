"""PuzzleMadness Palindrome Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 4, 1, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 6), (0, 5), (1, 4), (2, 5), (3, 6), (3, 7), (4, 6), (4, 7)])
    puzzle.add_palindrome([(5, 1), (6, 2), (6, 3), (5, 4), (4, 3)])
    puzzle.add_palindrome([(8, 8), (8, 7), (7, 6), (6, 5), (7, 5)])
    puzzle.add_palindrome([(3, 4), (3, 5), (2, 4), (1, 3), (2, 3)])
    puzzle.add_palindrome([(4, 4), (3, 3), (4, 2), (5, 2)])
    puzzle.add_palindrome([(6, 6), (5, 6), (4, 5)])
    puzzle.add_palindrome([(8, 2), (7, 2), (7, 3)])

    return puzzle
