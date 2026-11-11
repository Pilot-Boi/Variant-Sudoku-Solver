"""PuzzleMadness German Whispers Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 6, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 9, 1, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (1, 5), (1, 6), (2, 5), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(4, 1), (3, 2), (4, 3), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(5, 4), (6, 3), (7, 2), (8, 1), (7, 1)])
    puzzle.add_german_whispers([(6, 6), (7, 5), (8, 4), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(1, 1), (2, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(2, 7), (3, 6), (4, 7), (4, 6)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (5, 1)])

    return puzzle
