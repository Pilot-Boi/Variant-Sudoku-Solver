"""PuzzleMadness German Whispers Sudoku — 2025-06-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 2), (5, 3), (4, 3), (4, 2), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (1, 4), (2, 3), (3, 2)])
    puzzle.add_german_whispers([(7, 2), (7, 1), (6, 0), (5, 1), (4, 1)])
    puzzle.add_german_whispers([(5, 5), (6, 5), (6, 4), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (2, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (0, 2), (1, 1)])
    puzzle.add_german_whispers([(2, 4), (3, 3), (3, 4), (3, 5)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (8, 3), (8, 4)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8)])
    puzzle.add_german_whispers([(0, 6), (1, 5), (1, 6)])

    return puzzle
