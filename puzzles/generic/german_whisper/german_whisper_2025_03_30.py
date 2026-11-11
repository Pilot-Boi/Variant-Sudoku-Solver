"""PuzzleMadness German Whispers Sudoku — 2025-03-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 5, 3, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 3), (2, 3), (1, 2), (0, 3), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(2, 6), (3, 7), (3, 6), (3, 5), (4, 4)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 6), (2, 5), (1, 5)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 1), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(6, 6), (5, 6), (5, 7), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 7), (7, 6)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 8), (2, 7)])
    puzzle.add_german_whispers([(2, 2), (1, 1), (1, 0)])

    return puzzle
