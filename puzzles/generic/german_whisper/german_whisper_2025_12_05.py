"""PuzzleMadness German Whispers Sudoku — 2025-12-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 3, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (7, 1), (8, 2), (7, 3), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(1, 2), (2, 3), (2, 4), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(6, 5), (5, 6), (4, 6), (3, 5), (3, 4)])
    puzzle.add_german_whispers([(5, 1), (4, 0), (4, 1), (4, 2), (5, 3)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (1, 0), (0, 1)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(0, 7), (1, 6), (2, 6)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (3, 3)])
    puzzle.add_german_whispers([(6, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(4, 7), (3, 7), (3, 6)])

    return puzzle
