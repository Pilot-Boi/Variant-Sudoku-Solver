"""PuzzleMadness German Whispers Sudoku — 2025-11-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 8, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (1, 1), (2, 0), (3, 1), (4, 1), (4, 2)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (1, 6), (1, 5), (0, 4)])
    puzzle.add_german_whispers([(2, 1), (3, 2), (4, 3), (4, 4), (5, 5)])
    puzzle.add_german_whispers([(6, 4), (6, 3), (7, 4), (8, 3), (8, 2)])
    puzzle.add_german_whispers([(5, 6), (4, 6), (4, 5), (3, 6)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(1, 8), (0, 8), (1, 7), (0, 6)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (6, 1)])
    puzzle.add_german_whispers([(2, 4), (3, 5), (3, 4)])

    return puzzle
