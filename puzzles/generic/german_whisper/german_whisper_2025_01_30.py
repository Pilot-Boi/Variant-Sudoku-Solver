"""PuzzleMadness German Whispers Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 8), (5, 7), (4, 7), (3, 7), (2, 8), (1, 7)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (5, 1), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(7, 1), (8, 2), (8, 3), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(0, 7), (1, 6), (2, 6), (1, 5), (2, 5)])
    puzzle.add_german_whispers([(5, 3), (4, 4), (4, 3), (3, 2), (4, 2)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 0), (2, 1)])
    puzzle.add_german_whispers([(0, 5), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(4, 6), (5, 6), (6, 5)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 0)])

    return puzzle
