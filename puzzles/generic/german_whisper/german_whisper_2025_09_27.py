"""PuzzleMadness German Whispers Sudoku — 2025-09-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 1, 0, 3],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 6), (4, 7), (5, 7), (6, 6), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (8, 2), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(1, 2), (0, 3), (0, 4), (1, 4), (0, 5)])
    puzzle.add_german_whispers([(4, 1), (3, 1), (2, 1), (2, 2), (3, 3)])
    puzzle.add_german_whispers([(6, 5), (5, 4), (5, 3), (4, 3), (3, 2)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (6, 2), (7, 3)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (1, 6), (2, 5)])
    puzzle.add_german_whispers([(7, 8), (6, 7), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(2, 6), (3, 5), (3, 4)])

    return puzzle
