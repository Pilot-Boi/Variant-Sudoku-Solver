"""PuzzleMadness German Whispers Sudoku — 2025-02-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [9, 0, 0, 0, 0, 5, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 6), (1, 7), (2, 8), (3, 7), (4, 6), (5, 6)])
    puzzle.add_german_whispers([(2, 1), (3, 1), (3, 2), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(0, 4), (1, 3), (1, 4), (0, 5), (1, 5)])
    puzzle.add_german_whispers([(5, 2), (6, 3), (6, 4), (5, 5), (5, 4)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(6, 5), (7, 5), (7, 4), (7, 3)])
    puzzle.add_german_whispers([(7, 2), (8, 2), (8, 1), (7, 1)])
    puzzle.add_german_whispers([(4, 8), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(1, 0), (0, 1), (1, 2)])

    return puzzle
