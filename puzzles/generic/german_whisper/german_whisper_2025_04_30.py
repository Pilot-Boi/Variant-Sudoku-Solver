"""PuzzleMadness German Whispers Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 6), (2, 5), (1, 4), (2, 4), (3, 3), (3, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (6, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 0), (2, 0), (1, 1)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 6), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (2, 1), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(8, 7), (8, 8), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(4, 7), (4, 6), (3, 7), (2, 6)])
    puzzle.add_german_whispers([(5, 2), (5, 3), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(2, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(0, 3), (0, 4), (1, 3)])

    return puzzle
