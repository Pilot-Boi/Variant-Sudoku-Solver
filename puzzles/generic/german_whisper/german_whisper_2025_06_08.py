"""PuzzleMadness German Whispers Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 3, 4],
        [0, 4, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 6, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 2), (6, 1), (5, 1), (5, 2)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (1, 5), (2, 4), (1, 4)])
    puzzle.add_german_whispers([(1, 1), (2, 0), (1, 0), (0, 1), (0, 0)])
    puzzle.add_german_whispers([(7, 5), (6, 6), (6, 5), (5, 4), (6, 3)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(3, 5), (3, 4), (2, 5), (3, 6)])
    puzzle.add_german_whispers([(6, 8), (5, 8), (4, 7), (5, 6)])
    puzzle.add_german_whispers([(4, 2), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(7, 7), (7, 8), (8, 7)])

    return puzzle
