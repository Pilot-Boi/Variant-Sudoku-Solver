"""PuzzleMadness German Whispers Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 9, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 2, 0, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 7), (6, 8), (7, 8), (6, 7), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(2, 3), (3, 3), (4, 4), (5, 4), (5, 5)])
    puzzle.add_german_whispers([(1, 2), (2, 1), (1, 0), (0, 0), (1, 1)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (7, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (0, 6), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 3), (3, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 5), (7, 6), (7, 7)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 1), (4, 2)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (8, 3)])

    return puzzle
