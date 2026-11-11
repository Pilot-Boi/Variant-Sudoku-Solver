"""PuzzleMadness German Whispers Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0), (6, 0), (5, 1), (5, 2)])
    puzzle.add_german_whispers([(1, 5), (1, 4), (2, 3), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (2, 7), (1, 6), (1, 7)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (5, 7), (4, 7), (4, 8)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (8, 6), (7, 6), (7, 7)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(7, 3), (7, 2), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(5, 3), (4, 3), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(1, 2), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(4, 1), (4, 0), (3, 0)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(6, 3), (6, 4), (5, 4)])

    return puzzle
