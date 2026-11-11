"""PuzzleMadness German Whispers Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 2, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 5, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (0, 4), (0, 5), (1, 6), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (4, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (1, 1), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(8, 1), (7, 2), (7, 3), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(8, 3), (7, 4), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(4, 4), (4, 5), (3, 4), (3, 5)])
    puzzle.add_german_whispers([(7, 7), (7, 8), (6, 7), (6, 8)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (3, 6)])
    puzzle.add_german_whispers([(3, 1), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(5, 2), (4, 2), (4, 1)])

    return puzzle
