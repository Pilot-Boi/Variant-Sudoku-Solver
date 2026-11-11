"""PuzzleMadness German Whispers Sudoku — 2025-08-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 3, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (2, 5), (2, 6), (3, 6), (4, 7), (5, 7)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (7, 3), (6, 3), (5, 4)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (5, 1), (5, 0), (6, 0)])
    puzzle.add_german_whispers([(2, 7), (1, 8), (2, 8), (3, 7), (4, 8)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(2, 3), (3, 3), (2, 4), (1, 3)])
    puzzle.add_german_whispers([(7, 0), (6, 1), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(2, 2), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 7)])

    return puzzle
