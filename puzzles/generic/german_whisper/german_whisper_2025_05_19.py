"""PuzzleMadness German Whispers Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 5, 0, 7, 0],
        [5, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 5), (4, 4), (3, 5), (4, 6), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(8, 7), (7, 7), (6, 8), (6, 7), (5, 7)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (0, 2), (1, 3), (2, 4)])
    puzzle.add_german_whispers([(7, 4), (7, 5), (8, 5), (8, 4), (7, 3)])
    puzzle.add_german_whispers([(7, 1), (6, 0), (5, 0), (4, 1), (5, 2)])
    puzzle.add_german_whispers([(1, 2), (1, 1), (2, 2), (3, 3)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (1, 6), (1, 7)])
    puzzle.add_german_whispers([(7, 2), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(5, 4), (5, 5), (6, 6)])

    return puzzle
