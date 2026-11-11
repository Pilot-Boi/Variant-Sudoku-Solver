"""PuzzleMadness German Whispers Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 2), (8, 2), (7, 1), (6, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(5, 7), (6, 6), (7, 5), (6, 5), (5, 6)])
    puzzle.add_german_whispers([(3, 5), (2, 4), (1, 4), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (6, 3), (5, 3), (4, 2)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (4, 4), (5, 5)])
    puzzle.add_german_whispers([(8, 8), (7, 7), (8, 7), (7, 6)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (2, 3), (1, 3)])
    puzzle.add_german_whispers([(6, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (2, 7)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 6)])

    return puzzle
