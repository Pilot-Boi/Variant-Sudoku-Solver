"""PuzzleMadness German Whispers Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 9, 0, 6],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 7, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 2), (5, 1), (4, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (2, 6), (1, 6), (2, 7)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (7, 6), (8, 6), (7, 7)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (1, 1), (2, 2), (3, 3)])
    puzzle.add_german_whispers([(6, 1), (6, 2), (5, 3), (4, 4), (5, 5)])
    puzzle.add_german_whispers([(1, 4), (2, 4), (3, 5), (3, 4)])
    puzzle.add_german_whispers([(3, 7), (3, 8), (4, 7), (3, 6)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (0, 6)])

    return puzzle
