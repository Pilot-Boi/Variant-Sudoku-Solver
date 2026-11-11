"""PuzzleMadness German Whispers Sudoku — 2025-11-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 2, 7],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 6), (3, 6), (2, 7), (3, 7), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 2), (2, 1), (1, 1)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4), (7, 5), (8, 6)])
    puzzle.add_german_whispers([(2, 5), (2, 4), (3, 4), (4, 3), (3, 2)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (1, 6), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(4, 2), (5, 2), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (6, 6), (7, 6)])

    return puzzle
