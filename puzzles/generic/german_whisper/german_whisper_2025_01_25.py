"""PuzzleMadness German Whispers Sudoku — 2025-01-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 8, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 1), (1, 2), (2, 3), (2, 4), (3, 4), (4, 4)])
    puzzle.add_german_whispers([(2, 2), (3, 1), (3, 0), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 2), (6, 3), (5, 3)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (1, 5), (2, 6), (2, 7)])
    puzzle.add_german_whispers([(5, 6), (4, 7), (5, 7), (5, 8), (6, 7)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (6, 6), (6, 5)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (4, 2), (4, 1)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (0, 6), (1, 6)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (1, 3)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1)])

    return puzzle
