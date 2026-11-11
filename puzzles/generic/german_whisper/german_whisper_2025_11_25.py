"""PuzzleMadness German Whispers Sudoku — 2025-11-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 8), (4, 7), (4, 6), (3, 6), (4, 5), (5, 4)])
    puzzle.add_german_whispers([(3, 4), (3, 5), (2, 5), (1, 6), (0, 5)])
    puzzle.add_german_whispers([(7, 2), (6, 3), (6, 2), (6, 1), (7, 0)])
    puzzle.add_german_whispers([(1, 2), (0, 2), (0, 3), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(2, 2), (1, 1), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (4, 0)])
    puzzle.add_german_whispers([(8, 2), (7, 3), (7, 4)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (3, 7)])

    return puzzle
