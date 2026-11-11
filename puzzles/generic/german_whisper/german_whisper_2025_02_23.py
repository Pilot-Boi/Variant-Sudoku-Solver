"""PuzzleMadness German Whispers Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 9, 0],
        [0, 8, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 7), (8, 8), (7, 7), (8, 6), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(7, 1), (6, 2), (6, 3), (7, 3), (8, 4)])
    puzzle.add_german_whispers([(5, 6), (6, 5), (5, 5), (5, 4), (4, 3)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(1, 2), (1, 3), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(1, 7), (0, 7), (0, 6)])

    return puzzle
