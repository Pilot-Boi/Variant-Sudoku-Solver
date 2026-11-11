"""PuzzleMadness German Whispers Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 3, 8, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 4), (8, 5), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (0, 4), (1, 3), (1, 4)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (7, 0), (6, 1), (5, 0)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (5, 8), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(5, 2), (4, 2), (3, 2), (4, 3)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(3, 6), (3, 5), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(5, 6), (6, 7), (6, 6)])
    puzzle.add_german_whispers([(1, 7), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (8, 7)])

    return puzzle
