"""PuzzleMadness German Whispers Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 6, 0],
        [6, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 4), (1, 3), (1, 2), (0, 2), (0, 3), (1, 4)])
    puzzle.add_german_whispers([(4, 2), (3, 2), (3, 1), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (4, 4), (5, 5), (6, 6)])
    puzzle.add_german_whispers([(5, 1), (6, 1), (7, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(7, 6), (8, 5), (8, 4), (7, 3), (7, 4)])
    puzzle.add_german_whispers([(1, 1), (2, 2), (2, 3), (3, 4)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (1, 7), (1, 6)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(5, 3), (4, 3), (5, 4)])

    return puzzle
