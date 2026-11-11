"""PuzzleMadness German Whispers Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 3, 0, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 6), (3, 7), (4, 8), (5, 8), (4, 7), (5, 6)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (5, 3), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(8, 2), (8, 1), (7, 2), (6, 1), (5, 0)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (1, 7), (0, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 1), (3, 0), (2, 1), (1, 2)])
    puzzle.add_german_whispers([(0, 5), (1, 4), (0, 3), (0, 2)])
    puzzle.add_german_whispers([(1, 3), (2, 2), (2, 3), (3, 2)])
    puzzle.add_german_whispers([(7, 6), (8, 6), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (5, 7)])
    puzzle.add_german_whispers([(1, 0), (0, 0), (1, 1)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (5, 1)])

    return puzzle
