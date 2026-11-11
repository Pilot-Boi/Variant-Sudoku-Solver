"""PuzzleMadness German Whispers Sudoku — 2025-06-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 1), (6, 1), (7, 2), (8, 3), (7, 3), (6, 3)])
    puzzle.add_german_whispers([(1, 4), (0, 4), (1, 5), (2, 6), (3, 7)])
    puzzle.add_german_whispers([(6, 6), (6, 7), (7, 6), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(3, 2), (2, 2), (2, 1), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 7), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(5, 3), (5, 2), (4, 3), (4, 2)])
    puzzle.add_german_whispers([(5, 6), (4, 5), (4, 6), (3, 5)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 3)])
    puzzle.add_german_whispers([(8, 5), (7, 4), (8, 4)])

    return puzzle
