"""PuzzleMadness Palindrome Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 6, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 3],
        [0, 0, 0, 5, 0, 0, 8, 0, 9],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 5), (6, 5), (7, 4), (6, 4), (5, 3), (4, 4), (5, 4)])
    puzzle.add_palindrome([(3, 4), (4, 3), (3, 2), (2, 1), (1, 2), (0, 1)])
    puzzle.add_palindrome([(7, 1), (7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_palindrome([(3, 6), (2, 5), (1, 6), (0, 7), (0, 8)])
    puzzle.add_palindrome([(4, 0), (5, 1), (6, 2)])
    puzzle.add_palindrome([(5, 7), (6, 6), (7, 6)])

    return puzzle
