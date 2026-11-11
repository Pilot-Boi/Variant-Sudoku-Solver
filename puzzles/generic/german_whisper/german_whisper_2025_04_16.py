"""PuzzleMadness German Whispers Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 3, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 0), (4, 1), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(2, 3), (3, 4), (2, 4), (1, 3), (1, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 5), (8, 6), (7, 7), (7, 6)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (4, 4), (5, 4), (5, 5)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 8), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 1), (7, 0)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (2, 2), (2, 1)])
    puzzle.add_german_whispers([(8, 4), (8, 3), (7, 4), (7, 3)])
    puzzle.add_german_whispers([(2, 5), (3, 6), (4, 5)])

    return puzzle
