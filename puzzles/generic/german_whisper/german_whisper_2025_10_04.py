"""PuzzleMadness German Whispers Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 9],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 6), (6, 5), (7, 4), (7, 3), (8, 3), (8, 2)])
    puzzle.add_german_whispers([(3, 4), (2, 3), (3, 3), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (2, 7), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (5, 2), (6, 3), (6, 4)])
    puzzle.add_german_whispers([(2, 5), (1, 4), (2, 4), (3, 5)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (2, 1), (1, 2)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (7, 8)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (6, 1)])

    return puzzle
