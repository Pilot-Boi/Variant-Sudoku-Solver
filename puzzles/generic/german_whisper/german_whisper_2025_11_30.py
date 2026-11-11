"""PuzzleMadness German Whispers Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 3), (3, 3), (3, 4), (2, 5), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (4, 1), (5, 2), (6, 3)])
    puzzle.add_german_whispers([(6, 4), (5, 3), (4, 4), (4, 5), (5, 5)])
    puzzle.add_german_whispers([(3, 7), (4, 7), (5, 8), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(0, 7), (1, 6), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 1), (8, 2)])
    puzzle.add_german_whispers([(3, 5), (4, 6), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 5)])
    puzzle.add_german_whispers([(1, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(6, 2), (7, 3), (7, 4)])

    return puzzle
