"""PuzzleMadness German Whispers Sudoku — 2025-07-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 5, 6, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 8, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 3), (1, 3), (2, 2), (1, 1), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(7, 5), (7, 6), (6, 6), (6, 7), (5, 7)])
    puzzle.add_german_whispers([(5, 3), (5, 2), (6, 1), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(1, 5), (2, 4), (2, 3), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(6, 5), (5, 6), (4, 6), (4, 5)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(3, 8), (3, 7), (4, 7), (3, 6)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (1, 7)])
    puzzle.add_german_whispers([(1, 6), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(8, 7), (8, 8), (7, 7)])
    puzzle.add_german_whispers([(8, 5), (7, 4), (7, 3)])

    return puzzle
