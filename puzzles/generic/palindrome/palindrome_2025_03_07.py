"""PuzzleMadness Palindrome Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 1), (2, 2), (1, 2), (0, 2), (1, 3), (2, 3), (1, 4), (1, 5)])
    puzzle.add_palindrome([(4, 8), (5, 7), (4, 6), (3, 5), (3, 4)])
    puzzle.add_palindrome([(7, 1), (6, 0), (6, 1), (5, 1), (4, 2)])
    puzzle.add_palindrome([(6, 8), (7, 7), (6, 7), (5, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(7, 2), (6, 2), (5, 3), (5, 4)])
    puzzle.add_palindrome([(7, 6), (8, 6), (8, 5)])
    puzzle.add_palindrome([(1, 6), (2, 5), (2, 4)])

    return puzzle
