"""PuzzleMadness German Whispers Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [2, 4, 0, 8, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 8, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 7), (8, 6), (7, 5), (7, 4), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (2, 5), (1, 5), (1, 6)])
    puzzle.add_german_whispers([(5, 6), (6, 7), (6, 8), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(5, 4), (5, 3), (6, 2), (6, 1), (5, 1)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (7, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 7), (0, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(1, 2), (0, 2), (1, 3)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (3, 0)])
    puzzle.add_german_whispers([(3, 6), (4, 6), (3, 5)])

    return puzzle
