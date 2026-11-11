"""PuzzleMadness Palindrome Sudoku — 2025-04-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 2, 0, 5, 0, 6, 0, 0],
        [0, 0, 0, 0, 4, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 6, 0],
        [0, 0, 0, 0, 7, 5, 0, 0, 0],
        [8, 0, 7, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 7), (1, 7), (2, 6), (2, 5), (1, 5), (0, 4), (1, 3)])
    puzzle.add_palindrome([(6, 7), (7, 6), (8, 6), (8, 5), (8, 4)])
    puzzle.add_palindrome([(7, 4), (6, 3), (6, 4), (5, 4), (4, 5)])
    puzzle.add_palindrome([(3, 1), (4, 0), (5, 0), (6, 1), (6, 2)])
    puzzle.add_palindrome([(3, 5), (2, 4), (3, 3), (2, 3)])
    puzzle.add_palindrome([(3, 7), (3, 8), (2, 8)])
    puzzle.add_palindrome([(5, 3), (5, 2), (4, 2)])

    return puzzle
