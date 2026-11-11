"""PuzzleMadness Palindrome Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 9, 0, 7, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 7), (7, 8), (6, 7), (5, 7), (5, 6), (4, 5), (3, 5)])
    puzzle.add_palindrome([(5, 1), (6, 1), (6, 2), (7, 3), (8, 4), (8, 5)])
    puzzle.add_palindrome([(3, 1), (4, 2), (5, 2), (6, 3), (5, 3)])
    puzzle.add_palindrome([(4, 4), (4, 3), (5, 4), (6, 5), (6, 6), (7, 6)])
    puzzle.add_palindrome([(2, 8), (2, 7), (3, 8), (3, 7)])
    puzzle.add_palindrome([(0, 5), (0, 6), (1, 5), (2, 6)])
    puzzle.add_palindrome([(3, 2), (3, 3), (2, 4), (2, 5)])

    return puzzle
