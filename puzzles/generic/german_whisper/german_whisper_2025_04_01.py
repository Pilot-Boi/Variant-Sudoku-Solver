"""PuzzleMadness German Whispers Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 6), (3, 5), (3, 6), (2, 6), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (5, 4), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 5), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 7), (5, 6), (6, 6)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (3, 1), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (8, 0), (7, 0)])
    puzzle.add_german_whispers([(2, 7), (1, 7), (2, 8)])
    puzzle.add_german_whispers([(1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (4, 4)])

    return puzzle
