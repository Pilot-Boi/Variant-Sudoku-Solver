"""PuzzleMadness German Whispers Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 1), (4, 1), (4, 2), (3, 2), (2, 1), (1, 0)])
    puzzle.add_german_whispers([(2, 7), (1, 7), (0, 6), (1, 5), (2, 6)])
    puzzle.add_german_whispers([(6, 3), (7, 2), (8, 3), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (4, 6), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(1, 2), (1, 3), (2, 4), (2, 3)])
    puzzle.add_german_whispers([(5, 4), (4, 4), (3, 4), (2, 5)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1), (7, 1)])
    puzzle.add_german_whispers([(6, 8), (6, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (0, 1)])

    return puzzle
