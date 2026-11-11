"""PuzzleMadness German Whispers Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 9],
        [0, 7, 0, 0, 2, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 5), (7, 5), (7, 4), (6, 4), (5, 5), (4, 5)])
    puzzle.add_german_whispers([(1, 7), (2, 8), (1, 8), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (2, 2), (1, 3), (1, 4)])
    puzzle.add_german_whispers([(2, 5), (3, 6), (4, 7), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(4, 4), (5, 3), (5, 2), (4, 3)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 6), (6, 6)])
    puzzle.add_german_whispers([(5, 8), (6, 8), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(3, 0), (4, 1), (4, 2)])

    return puzzle
