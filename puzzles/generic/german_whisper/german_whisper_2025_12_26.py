"""PuzzleMadness German Whispers Sudoku — 2025-12-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 2), (1, 2), (1, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(8, 6), (7, 5), (6, 5), (5, 4), (4, 3)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (5, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (2, 8), (2, 7), (3, 6)])
    puzzle.add_german_whispers([(2, 2), (3, 1), (3, 2), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 2), (8, 1)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(6, 6), (5, 5), (4, 4)])

    return puzzle
