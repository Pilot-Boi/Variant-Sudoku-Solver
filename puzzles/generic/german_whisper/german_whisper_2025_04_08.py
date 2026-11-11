"""PuzzleMadness German Whispers Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 6), (3, 5), (4, 5), (4, 6), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (7, 3), (6, 3), (5, 4)])
    puzzle.add_german_whispers([(7, 0), (7, 1), (8, 0), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(1, 7), (1, 6), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(3, 1), (4, 1), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(2, 5), (3, 4), (3, 3), (2, 3)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(6, 7), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (1, 8)])

    return puzzle
