"""PuzzleMadness German Whispers Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 4, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 6, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 3],
        [0, 7, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 2, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 7), (2, 6), (1, 5), (2, 4), (2, 5), (3, 4)])
    puzzle.add_german_whispers([(6, 3), (7, 4), (8, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(6, 8), (5, 8), (4, 7), (5, 6), (6, 5)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 1), (7, 2)])
    puzzle.add_german_whispers([(6, 6), (6, 7), (7, 6), (8, 7)])

    return puzzle
