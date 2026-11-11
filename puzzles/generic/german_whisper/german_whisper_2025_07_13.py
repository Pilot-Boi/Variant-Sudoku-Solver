"""PuzzleMadness German Whispers Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 4), (1, 3), (2, 2), (3, 2), (4, 1), (4, 2)])
    puzzle.add_german_whispers([(4, 0), (5, 0), (5, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(3, 6), (4, 6), (5, 5), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(7, 7), (8, 8), (7, 8), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(2, 7), (3, 7), (2, 6), (3, 5), (4, 4)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (6, 1), (6, 2)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(0, 5), (1, 4), (0, 4)])

    return puzzle
