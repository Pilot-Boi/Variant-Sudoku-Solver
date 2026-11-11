"""PuzzleMadness German Whispers Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 4],
        [0, 0, 0, 0, 0, 7, 0, 8, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 2), (5, 1), (6, 2), (7, 2), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(2, 1), (1, 0), (0, 1), (1, 1), (2, 2)])
    puzzle.add_german_whispers([(0, 5), (0, 6), (1, 5), (2, 4), (2, 5)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (4, 3), (5, 2), (6, 3)])
    puzzle.add_german_whispers([(4, 7), (3, 7), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(8, 8), (7, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(8, 5), (7, 4), (7, 3), (8, 4)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (5, 8)])

    return puzzle
