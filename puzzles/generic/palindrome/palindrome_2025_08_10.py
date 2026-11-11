"""PuzzleMadness Palindrome Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 4, 9],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 2, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 2, 0, 0, 0, 0, 9, 4],
        [0, 0, 5, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(6, 1), (5, 2), (4, 1), (3, 2), (4, 3), (3, 3), (2, 4), (1, 3)])
    puzzle.add_palindrome([(4, 7), (3, 7), (4, 6), (4, 5), (3, 5)])
    puzzle.add_palindrome([(7, 7), (7, 6), (6, 5), (5, 4), (5, 3), (4, 2)])
    puzzle.add_palindrome([(5, 1), (5, 0), (6, 0)])
    puzzle.add_palindrome([(2, 7), (2, 6), (1, 5)])

    return puzzle
