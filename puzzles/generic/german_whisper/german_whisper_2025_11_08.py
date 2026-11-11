"""PuzzleMadness German Whispers Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 8), (1, 7), (0, 7), (1, 6), (2, 7), (3, 7)])
    puzzle.add_german_whispers([(5, 3), (6, 4), (7, 4), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(4, 1), (5, 0), (6, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(5, 6), (4, 5), (4, 6), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(2, 3), (3, 3), (2, 4), (2, 5), (3, 5)])
    puzzle.add_german_whispers([(1, 2), (2, 2), (3, 1), (4, 0)])
    puzzle.add_german_whispers([(8, 7), (7, 6), (6, 6), (5, 5)])
    puzzle.add_german_whispers([(5, 8), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(1, 5), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (3, 2)])

    return puzzle
