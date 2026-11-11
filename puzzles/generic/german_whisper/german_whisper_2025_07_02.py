"""PuzzleMadness German Whispers Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 8],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 4), (0, 3), (1, 3), (0, 2), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (4, 5), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(7, 2), (7, 3), (6, 2), (5, 1), (4, 1)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (6, 5), (5, 6), (6, 6)])
    puzzle.add_german_whispers([(6, 7), (5, 8), (5, 7), (4, 6)])
    puzzle.add_german_whispers([(3, 2), (2, 2), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (3, 5), (2, 4)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (8, 3)])

    return puzzle
