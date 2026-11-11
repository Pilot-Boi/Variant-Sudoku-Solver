"""PuzzleMadness Palindrome Sudoku — 2025-08-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-08-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/8/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 6, 0, 0, 0],
        [0, 0, 0, 8, 0, 9, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 7, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 6), (1, 5), (0, 4), (1, 3), (1, 2), (0, 2), (1, 1)])
    puzzle.add_palindrome([(3, 2), (3, 1), (4, 2), (5, 3), (5, 4), (6, 5)])
    puzzle.add_palindrome([(6, 4), (6, 3), (7, 3), (8, 2), (8, 1), (7, 1)])
    puzzle.add_palindrome([(4, 4), (5, 5), (5, 6), (6, 7), (5, 7)])
    puzzle.add_palindrome([(3, 5), (3, 6), (4, 7)])
    puzzle.add_palindrome([(5, 2), (6, 2), (5, 1), (6, 0)])
    puzzle.add_palindrome([(1, 6), (2, 7), (3, 8)])

    return puzzle
