"""PuzzleMadness German Whispers Sudoku — 2025-07-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 5, 8, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 4), (5, 5), (4, 4), (5, 3), (6, 2), (5, 2)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (1, 7), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (1, 2), (2, 3), (3, 4)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (8, 2), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (8, 6), (7, 5)])
    puzzle.add_german_whispers([(5, 7), (4, 8), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(2, 8), (2, 7), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(7, 0), (7, 1), (6, 1)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (5, 1)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (4, 2)])

    return puzzle
