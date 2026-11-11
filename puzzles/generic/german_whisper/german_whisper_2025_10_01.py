"""PuzzleMadness German Whispers Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 6, 0],
        [0, 7, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (8, 4), (8, 5), (7, 5), (8, 6), (8, 7)])
    puzzle.add_german_whispers([(1, 2), (1, 3), (0, 2), (1, 1), (2, 2)])
    puzzle.add_german_whispers([(4, 6), (5, 5), (5, 6), (6, 7), (6, 8)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (5, 1), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 6), (2, 6), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(2, 3), (3, 2), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(7, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(5, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(2, 1), (3, 1), (3, 0)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 5)])

    return puzzle
