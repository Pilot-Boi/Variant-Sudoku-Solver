"""PuzzleMadness German Whispers Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 7), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 8), (2, 7), (1, 6)])
    puzzle.add_german_whispers([(1, 2), (0, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(7, 4), (8, 3), (7, 3), (7, 2), (6, 3)])
    puzzle.add_german_whispers([(6, 5), (7, 6), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(4, 1), (5, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(3, 1), (4, 2), (5, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (3, 6)])
    puzzle.add_german_whispers([(4, 7), (5, 8), (6, 8)])

    return puzzle
