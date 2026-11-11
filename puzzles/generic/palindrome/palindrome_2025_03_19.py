"""PuzzleMadness Palindrome Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 4, 0, 2],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 2, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(1, 7), (1, 6), (2, 7), (2, 6), (3, 7), (4, 6), (4, 5), (3, 6)])
    puzzle.add_palindrome([(1, 1), (0, 1), (0, 2), (1, 3), (2, 4), (2, 3)])
    puzzle.add_palindrome([(5, 4), (4, 4), (3, 3), (4, 2), (5, 2), (6, 1)])
    puzzle.add_palindrome([(7, 2), (6, 3), (6, 4), (5, 5), (6, 6)])
    puzzle.add_palindrome([(3, 1), (2, 2), (1, 2)])
    puzzle.add_palindrome([(7, 4), (8, 3), (8, 2)])

    return puzzle
