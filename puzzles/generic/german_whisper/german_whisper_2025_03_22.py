"""PuzzleMadness German Whispers Sudoku — 2025-03-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 6, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 3, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 6), (6, 7), (5, 7), (4, 7), (4, 6), (3, 5)])
    puzzle.add_german_whispers([(7, 0), (7, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(5, 2), (6, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 4), (1, 3), (0, 3), (1, 2), (1, 1)])
    puzzle.add_german_whispers([(2, 2), (2, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(5, 5), (4, 4), (4, 5), (3, 4)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 5)])
    puzzle.add_german_whispers([(2, 6), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (7, 7)])

    return puzzle
