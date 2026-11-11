"""PuzzleMadness German Whispers Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 2, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 3), (7, 3), (8, 4), (7, 5), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 2), (5, 2), (5, 1)])
    puzzle.add_german_whispers([(3, 5), (2, 4), (3, 4), (3, 3), (2, 3)])
    puzzle.add_german_whispers([(2, 6), (1, 7), (2, 7), (3, 8)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (0, 4), (1, 4)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (5, 5)])
    puzzle.add_german_whispers([(3, 6), (4, 5), (4, 6)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (0, 3)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (7, 8)])

    return puzzle
