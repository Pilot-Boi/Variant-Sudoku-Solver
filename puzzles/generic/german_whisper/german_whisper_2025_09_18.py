"""PuzzleMadness German Whispers Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 1, 0],
        [0, 3, 0, 0, 0, 9, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 2), (6, 2), (6, 3), (7, 2), (6, 1), (5, 1)])
    puzzle.add_german_whispers([(8, 7), (7, 7), (6, 6), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(6, 4), (5, 4), (4, 3), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 0), (5, 0), (4, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(5, 7), (4, 6), (3, 7), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(1, 1), (0, 0), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(4, 8), (4, 7), (3, 8), (2, 8)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 6)])

    return puzzle
