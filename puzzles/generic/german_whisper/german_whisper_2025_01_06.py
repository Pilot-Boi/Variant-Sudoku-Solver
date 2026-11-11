"""PuzzleMadness German Whispers Sudoku — 2025-01-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 6, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (6, 4), (5, 3), (6, 3), (5, 2), (5, 1)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (3, 7), (4, 6), (3, 5)])
    puzzle.add_german_whispers([(7, 8), (6, 7), (7, 7), (7, 6), (8, 7)])
    puzzle.add_german_whispers([(2, 3), (3, 4), (2, 5), (1, 5), (1, 4)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 1), (1, 2), (1, 3)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 0), (8, 1)])
    puzzle.add_german_whispers([(2, 6), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(7, 5), (6, 5), (5, 4)])
    puzzle.add_german_whispers([(8, 3), (7, 2), (7, 1)])

    return puzzle
