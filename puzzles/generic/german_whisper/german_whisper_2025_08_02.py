"""PuzzleMadness German Whispers Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 4), (4, 5), (3, 6), (4, 6), (4, 7), (5, 7)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (1, 2), (2, 2), (2, 3)])
    puzzle.add_german_whispers([(5, 3), (6, 4), (7, 4), (7, 5), (8, 5)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (6, 7), (6, 6), (5, 6)])
    puzzle.add_german_whispers([(4, 3), (3, 4), (2, 4), (3, 5), (2, 5)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (5, 2), (4, 2)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (7, 1)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (2, 7)])
    puzzle.add_german_whispers([(3, 0), (4, 0), (4, 1)])

    return puzzle
