"""PuzzleMadness German Whispers Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 4, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 6, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 3), (1, 3), (1, 2), (2, 2), (2, 3), (3, 4)])
    puzzle.add_german_whispers([(3, 0), (4, 1), (5, 2), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (3, 6), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (6, 1), (7, 2), (8, 3)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (6, 4), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(0, 7), (1, 7), (1, 6), (2, 7)])
    puzzle.add_german_whispers([(2, 0), (3, 1), (2, 1)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (0, 1)])
    puzzle.add_german_whispers([(4, 4), (4, 5), (3, 5)])

    return puzzle
