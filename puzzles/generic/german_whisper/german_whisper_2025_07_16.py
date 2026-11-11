"""PuzzleMadness German Whispers Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 8],
        [9, 0, 0, 5, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 4), (2, 3), (2, 2), (3, 3), (3, 4), (4, 5)])
    puzzle.add_german_whispers([(5, 1), (4, 1), (3, 1), (4, 0), (3, 0)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (4, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(6, 5), (7, 6), (7, 7), (6, 6), (5, 5)])
    puzzle.add_german_whispers([(7, 2), (7, 1), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (1, 6), (0, 5)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (8, 4), (8, 3)])
    puzzle.add_german_whispers([(4, 3), (5, 4), (6, 4)])
    puzzle.add_german_whispers([(1, 1), (1, 0), (2, 0)])

    return puzzle
