"""PuzzleMadness German Whispers Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 3, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 7, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 6), (3, 7), (4, 8), (5, 8), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(5, 1), (6, 2), (5, 3), (4, 4), (3, 5)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 0), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (3, 3), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (8, 6), (8, 5), (7, 5)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 3), (6, 4)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_german_whispers([(4, 0), (4, 1), (3, 0), (3, 1)])
    puzzle.add_german_whispers([(1, 5), (1, 4), (0, 5)])

    return puzzle
