"""PuzzleMadness German Whispers Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 5), (7, 6), (7, 7), (6, 6), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(7, 0), (6, 0), (5, 0), (4, 1), (5, 1)])
    puzzle.add_german_whispers([(1, 2), (2, 2), (2, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(7, 2), (6, 1), (7, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(4, 2), (4, 3), (3, 3), (2, 4), (2, 5)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (6, 3), (5, 3)])
    puzzle.add_german_whispers([(4, 7), (3, 8), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(2, 7), (2, 6), (1, 5), (1, 6)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (0, 6), (0, 7)])

    return puzzle
