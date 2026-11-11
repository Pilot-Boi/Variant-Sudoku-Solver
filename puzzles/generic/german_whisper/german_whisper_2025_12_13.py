"""PuzzleMadness German Whispers Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 4, 0, 3, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 9, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [9, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 1), (4, 0), (3, 1), (3, 2), (3, 3), (2, 3)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 0), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (2, 5), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (6, 7), (5, 7), (6, 6)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(1, 1), (1, 2), (0, 2), (1, 3)])
    puzzle.add_german_whispers([(5, 4), (5, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 5), (6, 4), (6, 5)])

    return puzzle
