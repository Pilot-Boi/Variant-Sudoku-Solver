"""PuzzleMadness German Whispers Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 4],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 7), (3, 7), (3, 6), (2, 6), (2, 7), (3, 8)])
    puzzle.add_german_whispers([(8, 3), (7, 3), (6, 4), (5, 5), (4, 4)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (5, 1), (4, 1), (5, 2)])
    puzzle.add_german_whispers([(7, 7), (8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (2, 0), (3, 1)])
    puzzle.add_german_whispers([(2, 2), (1, 3), (0, 4), (1, 5)])
    puzzle.add_german_whispers([(1, 4), (2, 4), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(0, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 2)])
    puzzle.add_german_whispers([(6, 6), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (4, 3)])

    return puzzle
