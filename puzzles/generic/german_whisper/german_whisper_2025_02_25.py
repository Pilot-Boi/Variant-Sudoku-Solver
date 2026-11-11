"""PuzzleMadness German Whispers Sudoku — 2025-02-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 1],
        [0, 0, 4, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 7), (3, 8), (2, 7), (2, 6), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(1, 3), (2, 2), (2, 1), (1, 1), (0, 0)])
    puzzle.add_german_whispers([(3, 4), (3, 5), (2, 4), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(6, 2), (7, 3), (6, 4), (5, 5), (4, 6)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 5), (0, 4), (1, 4)])
    puzzle.add_german_whispers([(6, 7), (7, 8), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (4, 1), (4, 2)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 1)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (6, 5)])

    return puzzle
