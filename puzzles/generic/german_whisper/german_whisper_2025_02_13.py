"""PuzzleMadness German Whispers Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 4],
        [0, 4, 0, 0, 0, 0, 0, 7, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 0), (6, 1), (5, 1), (5, 2)])
    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 3), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (3, 0), (4, 1), (3, 1)])
    puzzle.add_german_whispers([(2, 4), (3, 3), (2, 3), (1, 4), (0, 5)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (0, 6), (1, 5), (2, 5)])
    puzzle.add_german_whispers([(6, 6), (7, 5), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (7, 7), (6, 7)])
    puzzle.add_german_whispers([(6, 5), (5, 6), (4, 7), (4, 6)])
    puzzle.add_german_whispers([(1, 1), (1, 2), (2, 2)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (3, 8)])

    return puzzle
