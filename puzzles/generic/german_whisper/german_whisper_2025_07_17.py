"""PuzzleMadness German Whispers Sudoku — 2025-07-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 7, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (6, 6), (6, 7), (5, 6), (5, 5), (4, 4)])
    puzzle.add_german_whispers([(2, 0), (2, 1), (1, 2), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (0, 6), (1, 5), (1, 4)])
    puzzle.add_german_whispers([(2, 8), (3, 8), (4, 8), (4, 7), (4, 6)])
    puzzle.add_german_whispers([(7, 4), (8, 3), (7, 2), (6, 1), (5, 1)])
    puzzle.add_german_whispers([(6, 3), (5, 2), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (3, 0), (3, 1)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(3, 6), (2, 5), (3, 5)])

    return puzzle
