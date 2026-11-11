"""PuzzleMadness German Whispers Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 2, 7, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 9, 0, 0, 2, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 8), (4, 7), (5, 8), (6, 7), (5, 6), (4, 6)])
    puzzle.add_german_whispers([(7, 7), (8, 6), (8, 5), (7, 4), (7, 5)])
    puzzle.add_german_whispers([(2, 2), (1, 1), (2, 0), (3, 1), (2, 1)])
    puzzle.add_german_whispers([(0, 2), (1, 3), (2, 4), (3, 4), (2, 3)])
    puzzle.add_german_whispers([(6, 0), (5, 1), (6, 1), (5, 2), (4, 3)])
    puzzle.add_german_whispers([(2, 5), (3, 5), (4, 5), (5, 4)])
    puzzle.add_german_whispers([(0, 5), (1, 6), (0, 6), (0, 7)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (7, 2), (6, 3)])

    return puzzle
