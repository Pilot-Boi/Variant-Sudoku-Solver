"""PuzzleMadness German Whispers Sudoku — 2025-02-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 8), (3, 8), (4, 7), (5, 6)])
    puzzle.add_german_whispers([(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(2, 4), (2, 3), (3, 2), (4, 2), (4, 3)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (6, 7), (7, 7), (7, 6)])
    puzzle.add_german_whispers([(5, 2), (5, 3), (4, 4), (4, 5)])
    puzzle.add_german_whispers([(7, 4), (8, 4), (7, 3), (6, 2)])
    puzzle.add_german_whispers([(2, 5), (3, 5), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(1, 3), (0, 4), (1, 4)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 7)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (5, 1)])

    return puzzle
