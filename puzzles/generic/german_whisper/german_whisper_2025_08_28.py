"""PuzzleMadness German Whispers Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0), (6, 0), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 4), (5, 5), (4, 6)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (2, 1), (3, 2), (4, 2)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (1, 5), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (3, 7), (4, 7), (4, 8)])
    puzzle.add_german_whispers([(1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(8, 3), (8, 2), (7, 2)])
    puzzle.add_german_whispers([(4, 5), (3, 5), (3, 4)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (0, 3)])

    return puzzle
