"""PuzzleMadness German Whispers Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 4, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [1, 7, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 6, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (6, 4), (5, 4), (4, 3), (3, 2), (2, 1)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (1, 3), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (8, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 2), (6, 1), (7, 1)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (5, 2), (4, 1)])
    puzzle.add_german_whispers([(2, 6), (3, 7), (4, 8), (4, 7)])
    puzzle.add_german_whispers([(2, 4), (3, 5), (4, 6), (5, 7)])
    puzzle.add_german_whispers([(3, 1), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(0, 6), (1, 7), (1, 8)])

    return puzzle
