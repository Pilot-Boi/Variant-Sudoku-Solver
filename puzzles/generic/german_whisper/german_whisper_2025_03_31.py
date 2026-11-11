"""PuzzleMadness German Whispers Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 4, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 5), (2, 6), (2, 7), (3, 7), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(8, 5), (8, 6), (7, 7), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(5, 4), (4, 3), (3, 2), (4, 2), (4, 1)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (7, 1), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(2, 4), (3, 3), (2, 3), (2, 2)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 2)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(1, 7), (1, 6), (0, 6)])

    return puzzle
