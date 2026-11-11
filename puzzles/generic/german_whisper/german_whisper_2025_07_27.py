"""PuzzleMadness German Whispers Sudoku — 2025-07-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 6), (4, 5), (4, 6), (5, 6), (4, 7), (5, 8)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (8, 1), (7, 2), (7, 3)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (8, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(6, 4), (5, 3), (4, 2), (3, 1), (3, 2)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (2, 1), (1, 2), (1, 1)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(4, 3), (5, 4), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(1, 5), (1, 6), (2, 7), (3, 8)])
    puzzle.add_german_whispers([(5, 1), (6, 2), (6, 3), (7, 4)])
    puzzle.add_german_whispers([(0, 1), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 7)])
    puzzle.add_german_whispers([(7, 8), (6, 8), (6, 7)])

    return puzzle
