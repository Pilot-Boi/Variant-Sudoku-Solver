"""PuzzleMadness Palindrome Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 1],
        [0, 0, 0, 1, 4, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 4, 0, 0, 0, 0, 3],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 3), (6, 4), (5, 4), (4, 3), (3, 2), (3, 1), (2, 0), (2, 1)])
    puzzle.add_palindrome([(8, 5), (8, 4), (7, 3), (8, 2), (7, 2), (6, 2)])
    puzzle.add_palindrome([(4, 7), (4, 6), (3, 6), (4, 5), (5, 5), (6, 5)])
    puzzle.add_palindrome([(5, 6), (6, 6), (7, 5)])
    puzzle.add_palindrome([(5, 7), (5, 8), (6, 7), (7, 6)])
    puzzle.add_palindrome([(7, 0), (6, 0), (5, 1), (5, 2)])

    return puzzle
