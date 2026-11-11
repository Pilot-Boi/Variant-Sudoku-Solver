"""PuzzleMadness German Whispers Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 6), (2, 6), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(5, 5), (4, 5), (4, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(0, 3), (1, 2), (1, 1), (2, 0), (3, 1)])
    puzzle.add_german_whispers([(8, 3), (7, 4), (8, 5), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (5, 8), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(7, 1), (8, 1), (8, 0), (7, 0)])
    puzzle.add_german_whispers([(6, 1), (5, 1), (5, 2), (6, 3)])
    puzzle.add_german_whispers([(2, 1), (2, 2), (3, 3), (3, 2)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (5, 4), (6, 5)])

    return puzzle
