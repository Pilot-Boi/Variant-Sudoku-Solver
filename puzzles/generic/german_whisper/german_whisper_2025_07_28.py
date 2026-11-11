"""PuzzleMadness German Whispers Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 5, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 6), (6, 6), (7, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 5), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(2, 0), (3, 1), (2, 2), (2, 3), (3, 2)])
    puzzle.add_german_whispers([(4, 1), (5, 2), (6, 3), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(4, 6), (3, 7), (4, 7), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (4, 3), (3, 3)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(1, 7), (0, 8), (1, 8)])
    puzzle.add_german_whispers([(7, 4), (8, 5), (8, 6)])

    return puzzle
