"""PuzzleMadness German Whispers Sudoku — 2025-01-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 1), (7, 2), (8, 2), (8, 3), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (2, 8), (3, 8), (4, 7)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 4), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (5, 1), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (7, 8), (8, 7)])
    puzzle.add_german_whispers([(2, 7), (3, 7), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(8, 5), (7, 6), (6, 6), (5, 6)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(0, 3), (1, 4), (0, 4)])

    return puzzle
