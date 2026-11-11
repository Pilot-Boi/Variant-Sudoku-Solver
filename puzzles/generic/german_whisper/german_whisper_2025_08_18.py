"""PuzzleMadness German Whispers Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 9, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 4), (4, 5), (4, 6), (3, 7), (4, 7), (5, 7)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (5, 3), (4, 3), (3, 4)])
    puzzle.add_german_whispers([(3, 5), (2, 5), (1, 5), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(2, 0), (3, 0), (2, 1), (2, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (6, 1), (5, 0)])
    puzzle.add_german_whispers([(6, 8), (7, 7), (6, 6), (6, 5)])
    puzzle.add_german_whispers([(2, 7), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 3)])

    return puzzle
