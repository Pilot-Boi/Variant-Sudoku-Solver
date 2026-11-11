"""PuzzleMadness Palindrome Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 7],
        [0, 0, 6, 0, 4, 2, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 4), (8, 4), (7, 5), (6, 6), (5, 7), (4, 6), (3, 5), (3, 6)])
    puzzle.add_palindrome([(3, 3), (4, 3), (5, 4), (6, 4), (6, 5)])
    puzzle.add_palindrome([(3, 7), (2, 7), (1, 6), (1, 5), (2, 6)])
    puzzle.add_palindrome([(1, 2), (2, 3), (3, 4), (4, 5), (5, 5)])
    puzzle.add_palindrome([(7, 7), (7, 6), (8, 5)])
    puzzle.add_palindrome([(8, 1), (8, 2), (7, 3)])
    puzzle.add_palindrome([(6, 1), (6, 0), (5, 0)])

    return puzzle
