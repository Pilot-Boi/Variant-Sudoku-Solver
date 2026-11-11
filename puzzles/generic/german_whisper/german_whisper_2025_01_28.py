"""PuzzleMadness German Whispers Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 1, 0, 0, 0, 9, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 6), (1, 7), (0, 7), (0, 6), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (3, 5), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (7, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(1, 3), (2, 3), (1, 2), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(6, 8), (5, 8), (5, 7), (4, 8)])
    puzzle.add_german_whispers([(1, 0), (2, 0), (3, 0), (3, 1)])
    puzzle.add_german_whispers([(8, 3), (7, 4), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (2, 4), (2, 5)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (8, 7)])

    return puzzle
