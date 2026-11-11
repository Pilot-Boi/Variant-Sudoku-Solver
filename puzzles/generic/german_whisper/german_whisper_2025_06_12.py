"""PuzzleMadness German Whispers Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 7],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 2), (6, 3), (5, 3), (5, 4), (6, 5), (7, 6)])
    puzzle.add_german_whispers([(2, 2), (1, 1), (0, 1), (1, 2), (1, 3)])
    puzzle.add_german_whispers([(2, 1), (3, 2), (4, 3), (3, 3), (2, 4)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 4), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (3, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (8, 7)])

    return puzzle
