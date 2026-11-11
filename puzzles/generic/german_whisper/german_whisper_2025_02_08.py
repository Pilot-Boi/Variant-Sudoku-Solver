"""PuzzleMadness German Whispers Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 2), (6, 3), (6, 4), (5, 5), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (3, 6), (2, 5), (1, 6)])
    puzzle.add_german_whispers([(5, 1), (4, 0), (4, 1), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (1, 2), (0, 3), (1, 3)])
    puzzle.add_german_whispers([(6, 1), (6, 2), (7, 1), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (8, 4), (7, 3)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(1, 4), (0, 5), (1, 5)])
    puzzle.add_german_whispers([(3, 3), (3, 4), (2, 4)])

    return puzzle
