"""PuzzleMadness German Whispers Sudoku — 2025-08-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 3), (6, 2), (6, 3), (7, 4), (8, 4), (7, 5)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (4, 6), (5, 6), (6, 7)])
    puzzle.add_german_whispers([(2, 3), (1, 3), (2, 2), (2, 1), (3, 2)])
    puzzle.add_german_whispers([(5, 1), (4, 1), (4, 0), (3, 1), (3, 0)])
    puzzle.add_german_whispers([(1, 5), (1, 6), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (2, 7), (1, 8)])
    puzzle.add_german_whispers([(3, 5), (4, 4), (3, 4), (2, 5)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(6, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (5, 7)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (8, 7)])

    return puzzle
