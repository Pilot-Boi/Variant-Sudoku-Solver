"""PuzzleMadness German Whispers Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 1), (5, 1), (6, 1), (7, 2), (7, 3), (6, 4)])
    puzzle.add_german_whispers([(5, 3), (4, 2), (4, 3), (3, 2), (2, 2)])
    puzzle.add_german_whispers([(5, 4), (5, 5), (4, 6), (5, 7), (6, 7)])
    puzzle.add_german_whispers([(2, 6), (1, 6), (2, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(1, 4), (0, 5), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 4), (7, 5)])
    puzzle.add_german_whispers([(1, 2), (2, 1), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(4, 7), (3, 6), (3, 7)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (8, 7)])

    return puzzle
