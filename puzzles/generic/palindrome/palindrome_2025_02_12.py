"""PuzzleMadness Palindrome Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 7, 4, 0, 0, 0, 0],
        [3, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 7, 8],
        [0, 0, 0, 0, 0, 9, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 3), (1, 2), (2, 2), (2, 3), (3, 3), (4, 3), (5, 2)])
    puzzle.add_palindrome([(3, 5), (4, 5), (3, 6), (2, 6), (2, 7)])
    puzzle.add_palindrome([(4, 2), (4, 1), (3, 0), (2, 1), (2, 0), (1, 0)])
    puzzle.add_palindrome([(2, 4), (1, 5), (0, 5), (0, 6), (0, 7)])
    puzzle.add_palindrome([(6, 5), (5, 5), (4, 6), (5, 6)])
    puzzle.add_palindrome([(7, 4), (7, 5), (6, 6), (5, 7)])

    return puzzle
