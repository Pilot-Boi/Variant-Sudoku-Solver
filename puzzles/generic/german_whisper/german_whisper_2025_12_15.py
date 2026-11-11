"""PuzzleMadness German Whispers Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 0), (4, 0), (4, 1), (4, 2), (3, 3), (2, 2)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (6, 2), (6, 3), (7, 3)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (0, 2), (1, 2), (2, 1)])
    puzzle.add_german_whispers([(2, 7), (1, 6), (2, 5), (2, 4), (3, 5)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(7, 6), (8, 6), (7, 7), (7, 8)])
    puzzle.add_german_whispers([(7, 2), (8, 3), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 5)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(4, 7), (3, 8), (3, 7)])

    return puzzle
