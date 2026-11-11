"""PuzzleMadness German Whispers Sudoku — 2025-06-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 4, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 5), (5, 6), (6, 6), (6, 5), (6, 4), (7, 5)])
    puzzle.add_german_whispers([(2, 4), (3, 5), (4, 6), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(0, 3), (1, 2), (2, 2), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(4, 3), (5, 3), (5, 2), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (8, 5), (8, 6)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 7), (7, 8), (6, 7)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(3, 0), (4, 0), (5, 0)])

    return puzzle
