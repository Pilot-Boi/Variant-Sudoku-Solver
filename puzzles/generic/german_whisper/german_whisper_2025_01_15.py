"""PuzzleMadness German Whispers Sudoku — 2025-01-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 9, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 5), (4, 4), (4, 5), (5, 6), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(6, 4), (7, 5), (8, 4), (7, 3), (6, 3)])
    puzzle.add_german_whispers([(7, 1), (6, 1), (6, 0), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(3, 3), (3, 4), (2, 3), (1, 4), (2, 5)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(6, 7), (7, 8), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(2, 6), (3, 6), (3, 7)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(4, 1), (3, 2), (4, 2)])

    return puzzle
