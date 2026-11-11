"""PuzzleMadness German Whispers Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 5, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 0), (2, 1), (1, 1), (0, 2), (1, 3), (2, 4)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (5, 1), (4, 1), (4, 2)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 5), (5, 6), (6, 6)])
    puzzle.add_german_whispers([(5, 3), (6, 2), (6, 3), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8), (6, 8)])
    puzzle.add_german_whispers([(2, 7), (3, 8), (4, 8), (4, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (2, 5), (1, 5)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (8, 0)])

    return puzzle
