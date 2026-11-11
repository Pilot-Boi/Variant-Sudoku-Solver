"""PuzzleMadness German Whispers Sudoku — 2025-04-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 6), (4, 7), (3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_german_whispers([(1, 3), (1, 4), (0, 4), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(4, 5), (4, 4), (5, 4), (4, 3), (4, 2)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (7, 3), (8, 3), (8, 4)])
    puzzle.add_german_whispers([(6, 8), (7, 7), (6, 7), (5, 6)])
    puzzle.add_german_whispers([(5, 1), (4, 0), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(2, 5), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (1, 2)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (7, 6)])

    return puzzle
