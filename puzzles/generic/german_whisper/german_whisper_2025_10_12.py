"""PuzzleMadness German Whispers Sudoku — 2025-10-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 0), (7, 1), (6, 2), (5, 1), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(7, 4), (6, 4), (7, 5), (6, 6), (5, 6)])
    puzzle.add_german_whispers([(1, 7), (2, 8), (3, 8), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (2, 3), (1, 2), (0, 1)])
    puzzle.add_german_whispers([(1, 5), (2, 5), (2, 4), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(1, 1), (2, 2), (2, 1)])
    puzzle.add_german_whispers([(1, 4), (0, 3), (0, 2)])

    return puzzle
