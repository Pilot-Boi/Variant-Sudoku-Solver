"""PuzzleMadness German Whispers Sudoku — 2025-07-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 1, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 1), (2, 2), (3, 2), (4, 1), (4, 2), (5, 1)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (6, 5), (7, 5), (6, 4)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (1, 3), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(2, 7), (2, 6), (3, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (2, 0), (1, 0), (2, 1)])
    puzzle.add_german_whispers([(5, 6), (4, 5), (3, 5), (2, 4)])
    puzzle.add_german_whispers([(6, 7), (6, 6), (7, 7), (8, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(0, 6), (1, 5), (1, 4)])
    puzzle.add_german_whispers([(6, 8), (5, 7), (5, 8)])

    return puzzle
