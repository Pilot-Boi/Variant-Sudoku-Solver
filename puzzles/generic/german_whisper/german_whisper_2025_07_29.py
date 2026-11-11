"""PuzzleMadness German Whispers Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 7), (7, 7), (6, 7), (7, 6), (7, 5), (6, 4)])
    puzzle.add_german_whispers([(5, 5), (5, 4), (4, 3), (3, 2), (3, 3)])
    puzzle.add_german_whispers([(0, 5), (0, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(7, 1), (6, 0), (5, 0), (5, 1), (6, 2)])
    puzzle.add_german_whispers([(2, 5), (3, 6), (4, 6), (4, 5)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(1, 3), (0, 2), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 0)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 4)])

    return puzzle
