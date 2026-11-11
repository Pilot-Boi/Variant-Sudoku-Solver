"""PuzzleMadness German Whispers Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 9],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (8, 5), (7, 6), (6, 7), (6, 8), (5, 7)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 5), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (5, 0), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(1, 4), (1, 5), (2, 4), (1, 3), (0, 2)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (2, 8), (2, 7), (3, 6)])
    puzzle.add_german_whispers([(6, 6), (5, 6), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 2), (2, 1)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(3, 0), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 3)])

    return puzzle
