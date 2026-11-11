"""PuzzleMadness German Whispers Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [9, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 2), (5, 1), (6, 1), (7, 0), (7, 1), (6, 2)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (1, 0), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (4, 6), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(4, 1), (3, 2), (2, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(7, 2), (7, 3), (6, 4), (5, 3)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(3, 8), (3, 7), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(7, 7), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (1, 8)])
    puzzle.add_german_whispers([(5, 4), (4, 4), (4, 5)])

    return puzzle
