"""PuzzleMadness Palindrome Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3, 0, 0, 7, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 9],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 7, 0, 2, 4],
        [0, 5, 0, 2, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(0, 2), (1, 1), (1, 2), (2, 2), (2, 3), (3, 2), (4, 1)])
    puzzle.add_palindrome([(3, 8), (4, 8), (5, 7), (6, 6), (6, 7)])
    puzzle.add_palindrome([(4, 7), (3, 7), (2, 7), (2, 8), (1, 8)])
    puzzle.add_palindrome([(6, 3), (7, 4), (6, 5), (5, 6), (4, 6), (5, 5)])
    puzzle.add_palindrome([(2, 0), (2, 1), (3, 0), (3, 1)])
    puzzle.add_palindrome([(2, 5), (3, 6), (4, 5), (4, 4)])
    puzzle.add_palindrome([(0, 4), (1, 5), (2, 6), (1, 6)])

    return puzzle
