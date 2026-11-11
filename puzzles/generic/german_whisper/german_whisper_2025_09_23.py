"""PuzzleMadness German Whispers Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 6, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (1, 3), (1, 4), (2, 4), (3, 4), (2, 5)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 7), (5, 7), (6, 6)])
    puzzle.add_german_whispers([(8, 3), (8, 2), (7, 1), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(1, 7), (2, 8), (3, 7), (3, 6), (3, 5)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 2), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (1, 1), (0, 0)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(4, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4)])

    return puzzle
