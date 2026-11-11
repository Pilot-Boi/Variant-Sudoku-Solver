"""PuzzleMadness German Whispers Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 2, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 1, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 2), (1, 2), (2, 1), (2, 2), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 7), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_german_whispers([(2, 5), (1, 4), (0, 4), (1, 5), (2, 6)])
    puzzle.add_german_whispers([(5, 7), (5, 6), (4, 6), (3, 5)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (6, 2), (6, 3)])
    puzzle.add_german_whispers([(4, 2), (5, 3), (4, 3), (4, 4)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (5, 8)])

    return puzzle
