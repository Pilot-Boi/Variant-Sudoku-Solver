"""PuzzleMadness German Whispers Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 4), (1, 4), (1, 3), (2, 2), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (4, 6), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (6, 2), (5, 2), (5, 3)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (1, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(5, 4), (4, 3), (4, 4), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (6, 6), (7, 5)])
    puzzle.add_german_whispers([(7, 2), (7, 1), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(7, 6), (8, 6), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(2, 7), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (8, 4)])
    puzzle.add_german_whispers([(0, 3), (1, 2), (0, 2)])

    return puzzle
