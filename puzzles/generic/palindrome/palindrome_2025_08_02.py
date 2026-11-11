"""PuzzleMadness Palindrome Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 9, 0, 8, 0, 6, 0, 0],
        [8, 0, 0, 0, 0, 7, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(8, 6), (7, 5), (7, 6), (6, 6), (6, 5), (5, 4), (5, 5)])
    puzzle.add_palindrome([(4, 7), (5, 7), (6, 7), (6, 8), (7, 8)])
    puzzle.add_palindrome([(3, 3), (2, 2), (3, 2), (4, 1), (4, 2)])
    puzzle.add_palindrome([(2, 4), (3, 5), (4, 6), (5, 6), (4, 5)])
    puzzle.add_palindrome([(7, 2), (6, 1), (5, 0), (4, 0)])
    puzzle.add_palindrome([(6, 3), (6, 2), (5, 1)])
    puzzle.add_palindrome([(2, 8), (3, 7), (3, 6)])

    return puzzle
