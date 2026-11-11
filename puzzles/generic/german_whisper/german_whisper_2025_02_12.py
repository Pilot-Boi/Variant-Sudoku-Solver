"""PuzzleMadness German Whispers Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 8), (4, 8), (4, 7), (5, 7), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(8, 2), (7, 3), (6, 3), (5, 3), (4, 3)])
    puzzle.add_german_whispers([(1, 0), (2, 0), (2, 1), (2, 2), (3, 3)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 1), (5, 1), (4, 0)])
    puzzle.add_german_whispers([(2, 7), (1, 6), (1, 5), (0, 6), (0, 7)])
    puzzle.add_german_whispers([(4, 5), (5, 4), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (1, 7)])
    puzzle.add_german_whispers([(7, 5), (8, 4), (8, 5)])

    return puzzle
