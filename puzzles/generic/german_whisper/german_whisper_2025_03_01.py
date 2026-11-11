"""PuzzleMadness German Whispers Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 8), (7, 7), (6, 6), (6, 5), (7, 5), (8, 6)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (3, 1), (2, 2), (1, 2)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (6, 1), (5, 2), (4, 2)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (2, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(5, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (4, 4), (4, 5)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(2, 3), (1, 4), (2, 5)])
    puzzle.add_german_whispers([(1, 3), (0, 4), (1, 5)])

    return puzzle
