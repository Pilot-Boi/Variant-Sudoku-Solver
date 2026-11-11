"""PuzzleMadness German Whispers Sudoku — 2025-08-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 6), (0, 7), (1, 7), (2, 6), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (1, 4), (2, 3), (2, 4)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (5, 1), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(7, 7), (6, 7), (6, 8), (5, 8), (4, 7)])
    puzzle.add_german_whispers([(7, 1), (8, 2), (7, 3), (6, 3), (6, 4)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (0, 0), (0, 1)])
    puzzle.add_german_whispers([(6, 6), (5, 5), (5, 6), (4, 5)])
    puzzle.add_german_whispers([(3, 8), (3, 7), (2, 8), (1, 8)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(5, 3), (4, 2), (5, 2)])

    return puzzle
