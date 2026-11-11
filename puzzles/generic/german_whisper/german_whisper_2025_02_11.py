"""PuzzleMadness German Whispers Sudoku — 2025-02-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 2, 0],
        [9, 8, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 2), (3, 1), (4, 1), (4, 0), (5, 1), (6, 1)])
    puzzle.add_german_whispers([(6, 4), (5, 5), (4, 4), (3, 3), (3, 2)])
    puzzle.add_german_whispers([(8, 8), (7, 7), (7, 6), (6, 5), (6, 6)])
    puzzle.add_german_whispers([(2, 2), (2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_german_whispers([(3, 6), (4, 6), (4, 7), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 8), (3, 8)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 5), (8, 4)])
    puzzle.add_german_whispers([(7, 3), (7, 2), (7, 1), (6, 2)])
    puzzle.add_german_whispers([(3, 4), (3, 5), (2, 4), (2, 5)])
    puzzle.add_german_whispers([(2, 1), (1, 2), (1, 1)])

    return puzzle
