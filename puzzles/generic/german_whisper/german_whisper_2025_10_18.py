"""PuzzleMadness German Whispers Sudoku — 2025-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 2), (1, 3), (1, 4), (2, 5)])
    puzzle.add_german_whispers([(8, 6), (8, 5), (7, 5), (7, 4), (6, 3)])
    puzzle.add_german_whispers([(5, 7), (6, 6), (6, 7), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (3, 3), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(2, 4), (3, 4), (4, 3), (4, 4)])
    puzzle.add_german_whispers([(6, 2), (7, 3), (7, 2), (8, 1)])
    puzzle.add_german_whispers([(4, 6), (5, 5), (4, 5)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(1, 6), (0, 5), (1, 5)])

    return puzzle
