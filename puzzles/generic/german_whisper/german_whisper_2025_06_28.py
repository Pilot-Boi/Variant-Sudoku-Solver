"""PuzzleMadness German Whispers Sudoku — 2025-06-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 6, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 5), (8, 6), (7, 5), (7, 6), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (2, 5), (3, 4), (4, 4)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (3, 5), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (1, 3), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (6, 1), (6, 2)])
    puzzle.add_german_whispers([(7, 2), (7, 3), (8, 2), (8, 1)])
    puzzle.add_german_whispers([(5, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (7, 8)])
    puzzle.add_german_whispers([(1, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 6)])

    return puzzle
