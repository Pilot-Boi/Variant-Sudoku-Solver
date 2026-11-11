"""PuzzleMadness German Whispers Sudoku — 2025-02-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 8, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 3, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 4), (1, 3), (1, 2), (2, 1), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (5, 8), (6, 8), (6, 7)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (7, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (5, 3), (6, 4)])
    puzzle.add_german_whispers([(7, 6), (8, 7), (8, 6), (7, 5)])
    puzzle.add_german_whispers([(4, 6), (5, 6), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (2, 5), (1, 5)])
    puzzle.add_german_whispers([(1, 7), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(5, 1), (4, 1), (3, 0)])
    puzzle.add_german_whispers([(7, 3), (7, 4), (6, 3)])

    return puzzle
