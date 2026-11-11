"""PuzzleMadness Palindrome Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/7/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 6, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 9, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (5, 4), (6, 4), (7, 3), (8, 2), (8, 1), (7, 1), (6, 2)])
    puzzle.add_palindrome([(3, 2), (3, 1), (3, 0), (2, 1), (2, 2), (2, 3)])
    puzzle.add_palindrome([(7, 2), (6, 3), (5, 2), (4, 2), (5, 1)])
    puzzle.add_palindrome([(1, 7), (2, 7), (2, 8), (3, 7), (4, 6), (3, 5)])
    puzzle.add_palindrome([(1, 5), (2, 5), (1, 6), (0, 7)])
    puzzle.add_palindrome([(6, 6), (5, 6), (6, 7), (5, 8)])
    puzzle.add_palindrome([(6, 0), (5, 0), (4, 1)])

    return puzzle
