"""PuzzleMadness German Whispers Sudoku — 2025-05-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 6, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 1), (1, 2), (2, 1), (3, 1), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (0, 4), (1, 5), (2, 6)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (7, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(5, 6), (4, 6), (3, 5), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 5), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (2, 3), (2, 4)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (2, 7), (1, 7)])
    puzzle.add_german_whispers([(6, 5), (5, 4), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(2, 0), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(6, 4), (6, 3), (7, 2)])
    puzzle.add_german_whispers([(0, 7), (1, 8), (0, 8)])

    return puzzle
