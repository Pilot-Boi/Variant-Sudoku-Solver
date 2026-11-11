"""PuzzleMadness German Whispers Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [5, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 5), (4, 5), (3, 4), (3, 3), (2, 2), (1, 1)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_german_whispers([(4, 6), (5, 7), (6, 6), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(6, 0), (5, 1), (6, 1), (7, 2), (6, 2)])
    puzzle.add_german_whispers([(1, 4), (2, 3), (1, 3), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(7, 3), (6, 3), (5, 4), (4, 4)])
    puzzle.add_german_whispers([(1, 0), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (8, 1)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (8, 3)])
    puzzle.add_german_whispers([(8, 6), (7, 7), (8, 7)])

    return puzzle
