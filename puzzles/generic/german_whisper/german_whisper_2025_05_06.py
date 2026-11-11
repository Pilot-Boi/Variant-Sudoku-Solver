"""PuzzleMadness German Whispers Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 2],
        [0, 0, 4, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 7), (6, 6), (6, 5), (5, 6), (4, 5), (3, 6)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (0, 3), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (0, 6), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(3, 5), (3, 4), (2, 5), (2, 4), (2, 3)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (8, 5), (7, 5)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (6, 1), (7, 2)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(5, 8), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (1, 8)])

    return puzzle
