"""PuzzleMadness German Whispers Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 8, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 7],
        [0, 0, 4, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 7, 0, 0, 0, 2],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 1), (3, 2), (3, 1), (4, 0), (5, 0), (5, 1)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (6, 8), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(5, 5), (4, 6), (3, 5), (4, 4), (4, 5)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (7, 2), (6, 1), (7, 1)])
    puzzle.add_german_whispers([(2, 3), (1, 2), (0, 2), (1, 3), (1, 4)])
    puzzle.add_german_whispers([(2, 4), (1, 5), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(3, 6), (2, 7), (2, 8), (1, 7)])
    puzzle.add_german_whispers([(8, 7), (7, 7), (7, 6)])

    return puzzle
