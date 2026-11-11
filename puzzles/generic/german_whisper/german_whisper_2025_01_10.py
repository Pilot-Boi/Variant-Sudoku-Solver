"""PuzzleMadness German Whispers Sudoku — 2025-01-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 8, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 5), (0, 5), (1, 6), (1, 7), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 3), (2, 2), (3, 1), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(6, 1), (5, 2), (4, 3), (3, 4), (2, 4)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (6, 8), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 4), (5, 4), (4, 5)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (4, 7), (3, 6)])
    puzzle.add_german_whispers([(1, 4), (0, 3), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (3, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 5), (7, 5), (8, 5)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 0)])

    return puzzle
