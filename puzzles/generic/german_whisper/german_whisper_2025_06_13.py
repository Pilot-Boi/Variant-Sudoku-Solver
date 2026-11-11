"""PuzzleMadness German Whispers Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 4, 9, 7, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 1), (6, 2), (5, 2), (4, 1), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (5, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(2, 5), (1, 6), (0, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(2, 1), (1, 0), (0, 1), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(6, 6), (7, 5), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(1, 5), (2, 4), (3, 3)])
    puzzle.add_german_whispers([(5, 5), (4, 6), (3, 6)])
    puzzle.add_german_whispers([(1, 4), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(7, 7), (8, 8), (7, 8)])

    return puzzle
