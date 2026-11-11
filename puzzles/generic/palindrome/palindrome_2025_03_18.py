"""PuzzleMadness Palindrome Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 9, 8],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 7), (7, 8), (8, 7), (8, 6), (7, 5), (7, 4), (6, 4), (5, 3)])
    puzzle.add_palindrome([(8, 2), (7, 3), (6, 2), (6, 1), (5, 1)])
    puzzle.add_palindrome([(6, 6), (5, 6), (6, 7), (6, 8), (5, 7)])
    puzzle.add_palindrome([(3, 1), (4, 2), (3, 2), (2, 3), (3, 3), (4, 3)])
    puzzle.add_palindrome([(4, 1), (3, 0), (2, 0)])
    puzzle.add_palindrome([(1, 5), (2, 6), (3, 6)])
    puzzle.add_palindrome([(5, 5), (4, 6), (4, 7)])

    return puzzle
