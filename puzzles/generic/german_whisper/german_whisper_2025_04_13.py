"""PuzzleMadness German Whispers Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 2), (2, 1), (1, 1), (1, 0), (0, 0), (0, 1)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (5, 8), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(1, 5), (1, 6), (2, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(5, 6), (5, 5), (4, 4), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(6, 3), (5, 2), (4, 1), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 6), (2, 5), (2, 4)])
    puzzle.add_german_whispers([(6, 4), (7, 4), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(5, 1), (6, 2), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(4, 3), (5, 4), (6, 5)])

    return puzzle
