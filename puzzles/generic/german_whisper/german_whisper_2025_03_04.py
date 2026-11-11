"""PuzzleMadness German Whispers Sudoku — 2025-03-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 2), (5, 3), (4, 4), (3, 4), (2, 3), (2, 4)])
    puzzle.add_german_whispers([(5, 8), (6, 7), (5, 7), (6, 6), (7, 5)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (4, 1), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(2, 7), (3, 7), (4, 7), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(7, 3), (8, 4), (8, 5), (7, 6)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(1, 4), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(5, 5), (6, 5), (7, 4)])

    return puzzle
