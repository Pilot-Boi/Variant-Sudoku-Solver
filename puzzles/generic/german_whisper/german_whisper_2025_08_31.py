"""PuzzleMadness German Whispers Sudoku — 2025-08-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 6, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 6],
        [0, 9, 0, 0, 0, 0, 6, 0, 0],
        [0, 8, 0, 4, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (1, 4), (2, 5), (1, 6), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(0, 3), (1, 2), (2, 1), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(8, 3), (7, 4), (7, 3), (7, 2), (6, 3)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (4, 2), (5, 1), (6, 1)])
    puzzle.add_german_whispers([(5, 5), (5, 4), (6, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(4, 6), (3, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (3, 3), (2, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(2, 3), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(8, 7), (8, 8), (7, 7)])

    return puzzle
