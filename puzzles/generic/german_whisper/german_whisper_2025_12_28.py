"""PuzzleMadness German Whispers Sudoku — 2025-12-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 4, 0, 0, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 4, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 6), (0, 5), (1, 5), (2, 4), (3, 4), (2, 3)])
    puzzle.add_german_whispers([(5, 7), (5, 8), (4, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(4, 0), (5, 0), (6, 1), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(5, 4), (6, 4), (7, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (4, 3), (4, 2)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (0, 2), (1, 2)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(8, 8), (7, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (7, 1)])

    return puzzle
