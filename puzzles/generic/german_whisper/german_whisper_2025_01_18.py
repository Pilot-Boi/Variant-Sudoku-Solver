"""PuzzleMadness German Whispers Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 3), (0, 4), (1, 5), (0, 5), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(5, 2), (4, 3), (3, 4), (2, 5), (2, 4)])
    puzzle.add_german_whispers([(1, 2), (1, 1), (2, 2), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(6, 6), (6, 5), (5, 4), (6, 3), (6, 4)])
    puzzle.add_german_whispers([(3, 7), (3, 6), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (8, 2), (8, 1)])
    puzzle.add_german_whispers([(0, 7), (1, 7), (0, 8), (1, 8)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (8, 7), (7, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (7, 1)])
    puzzle.add_german_whispers([(4, 5), (5, 5), (5, 6)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (0, 1)])

    return puzzle
