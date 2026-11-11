"""PuzzleMadness Palindrome Sudoku — 2025-11-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Palindrome Sudoku — 2025-11-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/palindromelinesudoku/hard/2025/11/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 1, 4, 0],
        [0, 8, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 5, 0, 9, 0],
        [0, 0, 0, 0, 7, 0, 0, 3, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_palindrome([(4, 5), (4, 4), (3, 3), (4, 3), (4, 2), (5, 1), (6, 0)])
    puzzle.add_palindrome([(5, 5), (5, 4), (6, 3), (7, 3), (7, 2)])
    puzzle.add_palindrome([(6, 7), (5, 6), (6, 5), (7, 4), (7, 5)])
    puzzle.add_palindrome([(7, 6), (8, 5), (8, 4)])
    puzzle.add_palindrome([(6, 1), (6, 2), (5, 3)])

    return puzzle
