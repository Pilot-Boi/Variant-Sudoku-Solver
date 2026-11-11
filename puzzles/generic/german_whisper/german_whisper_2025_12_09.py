"""PuzzleMadness German Whispers Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 0), (7, 0), (6, 0), (6, 1), (6, 2), (5, 2)])
    puzzle.add_german_whispers([(4, 7), (3, 8), (3, 7), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 3), (1, 2), (1, 1), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(4, 3), (3, 2), (3, 1), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(5, 7), (4, 6), (5, 5), (5, 4), (6, 3)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(4, 5), (3, 4), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(2, 7), (1, 6), (2, 6), (1, 5)])
    puzzle.add_german_whispers([(7, 5), (7, 4), (7, 3), (8, 4)])

    return puzzle
