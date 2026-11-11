"""PuzzleMadness German Whispers Sudoku — 2025-09-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 5, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (1, 3), (0, 2), (1, 1), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 2), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(4, 7), (5, 6), (6, 6), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 7), (7, 7), (8, 6)])
    puzzle.add_german_whispers([(2, 5), (3, 4), (3, 3), (4, 2), (5, 3)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (3, 6), (4, 5)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 4)])
    puzzle.add_german_whispers([(6, 0), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (4, 0)])

    return puzzle
