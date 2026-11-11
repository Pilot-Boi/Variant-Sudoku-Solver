"""PuzzleMadness German Whispers Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 6, 0, 0, 9],
        [9, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 1), (7, 2), (8, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (2, 1), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (7, 7), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(1, 5), (2, 4), (2, 5), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (6, 4), (5, 4)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 6), (4, 5), (4, 4), (5, 5)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (4, 1)])
    puzzle.add_german_whispers([(4, 6), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (8, 5)])

    return puzzle
