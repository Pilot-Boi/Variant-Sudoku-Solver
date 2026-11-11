"""PuzzleMadness Palindrome Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [8, 0, 2, 0, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 3, 0, 8, 0, 0, 5],
        [0, 0, 0, 0, 6, 0, 3, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(3, 0), (3, 1), (4, 0), (5, 1), (6, 1), (7, 2), (8, 2)])
    puzzle.add_palindrome([(5, 2), (6, 2), (7, 3), (8, 4), (8, 3)])
    puzzle.add_palindrome([(2, 5), (2, 4), (1, 3), (1, 2), (1, 1)])
    puzzle.add_palindrome([(6, 5), (7, 5), (8, 6)])
    puzzle.add_palindrome([(7, 4), (6, 4), (5, 3), (4, 3)])

    return puzzle
