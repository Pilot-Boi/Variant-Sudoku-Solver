"""PuzzleMadness German Whispers Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 4, 9, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 0, 0, 0, 2, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 0), (3, 1), (2, 1), (1, 2), (0, 2), (0, 1)])
    puzzle.add_german_whispers([(4, 6), (3, 6), (2, 7), (2, 8), (3, 8)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 2), (7, 3), (6, 3)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (2, 4), (2, 5), (3, 5)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (6, 7), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(4, 4), (5, 5), (5, 4), (5, 3)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 1)])
    puzzle.add_german_whispers([(1, 7), (0, 7), (1, 8)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4)])

    return puzzle
