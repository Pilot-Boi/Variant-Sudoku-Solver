"""PuzzleMadness Palindrome Sudoku — 2025-06-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-06-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/6/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
        [0, 5, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 8],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 2, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(7, 2), (7, 1), (7, 0), (6, 0), (5, 1), (5, 0), (4, 1)])
    puzzle.add_palindrome([(5, 4), (5, 3), (6, 3), (7, 4), (6, 5)])
    puzzle.add_palindrome([(4, 4), (4, 5), (3, 5), (2, 4), (2, 3), (2, 2)])
    puzzle.add_palindrome([(6, 7), (7, 8), (6, 8), (5, 7), (4, 8)])
    puzzle.add_palindrome([(8, 4), (7, 3), (6, 2)])
    puzzle.add_palindrome([(4, 2), (4, 3), (3, 3)])
    puzzle.add_palindrome([(3, 6), (2, 5), (1, 6), (1, 5)])

    return puzzle
