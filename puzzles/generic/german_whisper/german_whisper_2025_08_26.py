"""PuzzleMadness German Whispers Sudoku — 2025-08-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 7, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 1), (2, 2), (3, 2), (3, 3), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(3, 6), (2, 5), (1, 4), (0, 3), (1, 3)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 7), (2, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (5, 7), (5, 6), (6, 6)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 6), (8, 7)])
    puzzle.add_german_whispers([(6, 2), (5, 2), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(3, 5), (3, 4), (4, 5), (4, 6)])
    puzzle.add_german_whispers([(2, 1), (3, 1), (4, 1), (4, 0)])

    return puzzle
