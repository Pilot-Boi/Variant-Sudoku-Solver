"""PuzzleMadness German Whispers Sudoku — 2025-04-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 2), (1, 3), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(5, 5), (4, 5), (3, 5), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (2, 7), (1, 6), (1, 7)])
    puzzle.add_german_whispers([(7, 4), (8, 4), (7, 5), (8, 6), (7, 7)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (4, 3), (5, 4)])
    puzzle.add_german_whispers([(2, 1), (3, 0), (4, 0), (5, 1)])
    puzzle.add_german_whispers([(5, 6), (5, 7), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (8, 1), (7, 0)])

    return puzzle
