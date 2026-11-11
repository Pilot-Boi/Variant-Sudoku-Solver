"""PuzzleMadness German Whispers Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 9, 5, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (7, 6), (6, 6), (5, 5), (5, 6), (6, 7)])
    puzzle.add_german_whispers([(1, 4), (0, 4), (1, 3), (0, 2), (0, 1)])
    puzzle.add_german_whispers([(2, 7), (1, 8), (2, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(4, 2), (4, 3), (3, 4), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(6, 3), (7, 2), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (1, 7)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (8, 3)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (1, 1)])

    return puzzle
