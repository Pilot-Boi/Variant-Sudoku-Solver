"""PuzzleMadness German Whispers Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 5, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 0), (3, 0), (4, 1), (5, 1), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(1, 4), (2, 3), (3, 3), (4, 4), (3, 5)])
    puzzle.add_german_whispers([(3, 7), (3, 6), (2, 5), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(5, 7), (4, 8), (5, 8), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (2, 2), (1, 3)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(5, 4), (4, 3), (3, 2)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(6, 0), (5, 0), (4, 0)])

    return puzzle
