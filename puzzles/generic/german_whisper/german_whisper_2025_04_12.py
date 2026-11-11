"""PuzzleMadness German Whispers Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 3), (7, 2), (6, 1), (5, 1), (4, 1), (3, 1)])
    puzzle.add_german_whispers([(2, 3), (3, 2), (3, 3), (4, 3), (5, 4)])
    puzzle.add_german_whispers([(2, 5), (3, 5), (4, 5), (4, 6), (5, 5)])
    puzzle.add_german_whispers([(7, 4), (6, 4), (6, 5), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (0, 6), (0, 7), (1, 7)])
    puzzle.add_german_whispers([(7, 6), (7, 7), (6, 8), (6, 7)])
    puzzle.add_german_whispers([(0, 4), (1, 4), (0, 3), (1, 3)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (8, 5)])

    return puzzle
