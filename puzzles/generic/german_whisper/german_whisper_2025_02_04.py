"""PuzzleMadness German Whispers Sudoku — 2025-02-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 1), (7, 2), (6, 2), (6, 3), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(4, 7), (5, 8), (6, 8), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(0, 5), (1, 5), (2, 5), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (1, 0), (0, 1), (0, 0)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (1, 7), (2, 7)])
    puzzle.add_german_whispers([(7, 6), (6, 6), (5, 5), (5, 6)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4), (7, 5)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (8, 1)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (4, 5)])

    return puzzle
