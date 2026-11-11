"""PuzzleMadness German Whispers Sudoku — 2025-06-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 8), (5, 8), (5, 7), (6, 7), (5, 6), (4, 5)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (0, 5), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(7, 0), (6, 0), (6, 1), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (3, 2), (2, 1), (1, 0)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (5, 1), (5, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 4), (7, 3), (6, 3)])
    puzzle.add_german_whispers([(3, 5), (2, 5), (2, 4), (1, 4)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (3, 7)])
    puzzle.add_german_whispers([(1, 2), (0, 1), (1, 1)])

    return puzzle
