"""PuzzleMadness German Whispers Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [2, 0, 4, 0, 0, 0, 0, 0, 1],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 4), (3, 4), (4, 4), (3, 5), (4, 6), (5, 7)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (5, 3), (6, 4), (7, 3)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 7), (7, 8), (6, 8)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(1, 7), (0, 6), (0, 5), (1, 5)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(2, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (4, 0)])

    return puzzle
