"""PuzzleMadness German Whispers Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 1, 0, 4],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 2, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 2), (8, 2), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(1, 6), (2, 7), (3, 8), (4, 8), (4, 7)])
    puzzle.add_german_whispers([(5, 2), (4, 3), (5, 3), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(3, 5), (3, 6), (2, 5), (3, 4), (2, 3)])
    puzzle.add_german_whispers([(3, 1), (3, 0), (2, 1), (1, 1), (0, 1)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(6, 5), (6, 4), (5, 5), (4, 6)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 2)])
    puzzle.add_german_whispers([(8, 6), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (0, 6)])
    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 0)])

    return puzzle
