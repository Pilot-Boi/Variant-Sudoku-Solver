"""PuzzleMadness German Whispers Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 7, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (6, 3), (5, 2), (5, 1), (6, 1), (7, 2)])
    puzzle.add_german_whispers([(6, 8), (5, 7), (4, 7), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (3, 5), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (0, 4), (1, 4), (2, 5)])
    puzzle.add_german_whispers([(2, 1), (1, 2), (0, 2), (1, 1)])
    puzzle.add_german_whispers([(0, 7), (1, 7), (0, 6), (0, 5)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (3, 8), (2, 7)])
    puzzle.add_german_whispers([(1, 0), (2, 0), (3, 1)])

    return puzzle
