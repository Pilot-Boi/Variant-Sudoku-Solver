"""PuzzleMadness German Whispers Sudoku — 2025-05-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 8],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (2, 3), (3, 2), (3, 3), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(3, 7), (3, 6), (4, 6), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(5, 3), (5, 2), (6, 1), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 6), (6, 6), (5, 7)])
    puzzle.add_german_whispers([(7, 3), (6, 3), (5, 4), (5, 5), (6, 4)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (2, 2), (2, 1)])
    puzzle.add_german_whispers([(0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (1, 2), (0, 1)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1)])
    puzzle.add_german_whispers([(6, 7), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (3, 8)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (7, 5)])

    return puzzle
