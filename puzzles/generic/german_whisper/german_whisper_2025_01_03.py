"""PuzzleMadness German Whispers Sudoku — 2025-01-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 8, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 5), (2, 4), (2, 3), (1, 2)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (2, 2), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(5, 7), (4, 7), (5, 6), (4, 5), (4, 4)])
    puzzle.add_german_whispers([(8, 4), (7, 5), (6, 6), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (6, 2), (5, 1)])
    puzzle.add_german_whispers([(3, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(5, 2), (4, 3), (5, 4), (6, 4)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(8, 3), (8, 2), (8, 1)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (2, 1)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (1, 8)])

    return puzzle
