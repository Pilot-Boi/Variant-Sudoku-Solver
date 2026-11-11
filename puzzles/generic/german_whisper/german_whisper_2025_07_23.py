"""PuzzleMadness German Whispers Sudoku — 2025-07-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 7, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 1), (2, 1), (3, 2)])
    puzzle.add_german_whispers([(6, 4), (6, 3), (5, 4), (4, 5), (4, 4)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (5, 1), (6, 0), (6, 1)])
    puzzle.add_german_whispers([(5, 6), (5, 5), (4, 6), (3, 7)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (7, 3), (7, 4)])
    puzzle.add_german_whispers([(7, 7), (6, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(3, 5), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 7)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (8, 1)])

    return puzzle
