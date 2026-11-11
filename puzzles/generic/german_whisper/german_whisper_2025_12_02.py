"""PuzzleMadness German Whispers Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 8],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (5, 6), (6, 6), (7, 5), (8, 6), (8, 7)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (3, 1), (4, 0), (5, 1)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (5, 5), (6, 4), (6, 3)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (1, 7), (2, 6), (3, 7)])
    puzzle.add_german_whispers([(0, 4), (1, 3), (1, 4), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (0, 3), (1, 2)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0), (7, 1)])
    puzzle.add_german_whispers([(5, 7), (4, 7), (5, 8)])

    return puzzle
