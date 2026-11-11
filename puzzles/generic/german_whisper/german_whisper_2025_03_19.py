"""PuzzleMadness German Whispers Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [3, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 7), (2, 6), (3, 6), (3, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(1, 0), (0, 0), (1, 1), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(8, 1), (7, 2), (7, 3), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(5, 2), (4, 2), (3, 3), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(7, 5), (7, 6), (8, 7), (7, 7), (6, 6)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (3, 5), (4, 6)])
    puzzle.add_german_whispers([(0, 4), (1, 4), (0, 3)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(6, 0), (5, 0), (4, 0)])

    return puzzle
