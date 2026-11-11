"""PuzzleMadness German Whispers Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 2, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 6), (4, 5), (3, 4), (2, 4), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 5), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(3, 3), (2, 2), (2, 1), (1, 0), (1, 1)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (6, 6), (5, 6)])
    puzzle.add_german_whispers([(5, 4), (6, 4), (7, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (5, 7), (6, 7)])
    puzzle.add_german_whispers([(3, 6), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(5, 1), (4, 2), (3, 1)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 2)])

    return puzzle
