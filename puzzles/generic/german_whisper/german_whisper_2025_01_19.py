"""PuzzleMadness German Whispers Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 7, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 6), (6, 5), (5, 5), (4, 4), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 7), (2, 6), (1, 7)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (1, 1), (0, 2), (1, 3)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (5, 2), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(2, 0), (2, 1), (3, 1), (3, 2)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 5), (1, 4)])
    puzzle.add_german_whispers([(4, 7), (3, 7), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(8, 3), (7, 3), (7, 2)])
    puzzle.add_german_whispers([(7, 1), (6, 0), (7, 0)])

    return puzzle
