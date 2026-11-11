"""PuzzleMadness German Whispers Sudoku — 2025-01-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 2, 0, 7, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 1, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 3), (0, 3), (0, 2), (1, 1), (1, 2), (2, 2)])
    puzzle.add_german_whispers([(7, 2), (8, 2), (7, 1), (7, 0), (6, 1)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (7, 3), (8, 4), (7, 5)])
    puzzle.add_german_whispers([(8, 6), (7, 6), (6, 6), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(3, 0), (4, 0), (4, 1), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (1, 7), (2, 7)])
    puzzle.add_german_whispers([(3, 5), (2, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (4, 7)])

    return puzzle
