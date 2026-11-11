"""PuzzleMadness German Whispers Sudoku — 2025-12-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 9, 7, 0, 0, 5],
        [0, 0, 6, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 8), (5, 7), (5, 6), (5, 5), (6, 5), (7, 4)])
    puzzle.add_german_whispers([(7, 3), (8, 4), (7, 5), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(4, 4), (5, 3), (6, 3), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (3, 1), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 3), (1, 4), (2, 4), (1, 5), (2, 5)])
    puzzle.add_german_whispers([(0, 5), (1, 6), (0, 7), (1, 8)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (8, 8)])

    return puzzle
