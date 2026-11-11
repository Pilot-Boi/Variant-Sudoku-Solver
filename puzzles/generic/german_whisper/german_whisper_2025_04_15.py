"""PuzzleMadness German Whispers Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 6, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 3), (7, 2), (6, 2), (5, 1), (5, 0), (6, 0)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 3), (8, 3), (8, 2)])
    puzzle.add_german_whispers([(4, 4), (4, 5), (5, 6), (6, 6), (7, 7)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (3, 7), (4, 7), (4, 8)])
    puzzle.add_german_whispers([(1, 5), (1, 4), (2, 5), (3, 5)])
    puzzle.add_german_whispers([(1, 3), (0, 3), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (5, 4), (5, 3)])
    puzzle.add_german_whispers([(3, 3), (2, 2), (1, 1)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 6), (0, 6), (0, 7)])

    return puzzle
