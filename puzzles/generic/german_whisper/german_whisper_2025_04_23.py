"""PuzzleMadness German Whispers Sudoku — 2025-04-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 8, 0, 0, 1, 7, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 2), (5, 1), (4, 2), (3, 1), (2, 1), (1, 2)])
    puzzle.add_german_whispers([(6, 1), (7, 2), (8, 1), (8, 2), (7, 3)])
    puzzle.add_german_whispers([(2, 7), (2, 6), (1, 6), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (7, 8), (6, 7), (5, 8)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (0, 3), (1, 3), (1, 4)])
    puzzle.add_german_whispers([(4, 6), (4, 7), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(3, 6), (4, 5), (3, 4), (3, 3)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (2, 0)])

    return puzzle
