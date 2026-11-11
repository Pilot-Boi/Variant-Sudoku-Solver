"""PuzzleMadness German Whispers Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 7, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (3, 1), (2, 0), (1, 1), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(2, 5), (1, 5), (0, 6), (0, 5), (1, 4)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (7, 2), (8, 3), (8, 2)])
    puzzle.add_german_whispers([(6, 3), (6, 4), (7, 5), (8, 6), (7, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (5, 2), (4, 1)])
    puzzle.add_german_whispers([(3, 6), (3, 5), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (8, 1)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (6, 8)])

    return puzzle
