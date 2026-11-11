"""PuzzleMadness German Whispers Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 7],
        [0, 0, 0, 5, 1, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (2, 5), (1, 6), (0, 5), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(2, 2), (2, 3), (3, 3), (4, 2), (4, 1)])
    puzzle.add_german_whispers([(3, 5), (4, 6), (4, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 5), (6, 4), (5, 4)])
    puzzle.add_german_whispers([(8, 2), (8, 1), (8, 0), (7, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (1, 2), (1, 3)])
    puzzle.add_german_whispers([(7, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (2, 6)])
    puzzle.add_german_whispers([(6, 2), (5, 1), (5, 2)])

    return puzzle
