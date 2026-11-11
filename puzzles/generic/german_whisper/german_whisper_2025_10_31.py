"""PuzzleMadness German Whispers Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 1, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 8), (2, 8), (2, 7), (3, 6), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8), (6, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 3), (7, 2), (6, 1), (7, 0), (8, 1)])
    puzzle.add_german_whispers([(7, 4), (7, 5), (6, 6), (7, 7), (6, 7)])
    puzzle.add_german_whispers([(6, 0), (5, 0), (4, 1), (3, 0)])
    puzzle.add_german_whispers([(1, 3), (2, 2), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(5, 3), (4, 4), (4, 5), (5, 4)])
    puzzle.add_german_whispers([(1, 6), (0, 6), (1, 5)])
    puzzle.add_german_whispers([(2, 4), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (1, 0)])

    return puzzle
