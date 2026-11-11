"""PuzzleMadness German Whispers Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 1), (4, 2), (3, 1), (2, 1), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(6, 7), (7, 6), (8, 7), (8, 6), (7, 5)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 2), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(4, 3), (5, 2), (5, 3), (4, 4), (3, 3)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (1, 3), (2, 2)])
    puzzle.add_german_whispers([(7, 4), (6, 3), (6, 4), (5, 4)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (3, 7), (3, 6)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (1, 6)])
    puzzle.add_german_whispers([(4, 8), (3, 8), (2, 8)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(5, 6), (6, 5), (5, 5)])

    return puzzle
