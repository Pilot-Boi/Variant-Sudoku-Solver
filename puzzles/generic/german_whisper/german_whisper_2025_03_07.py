"""PuzzleMadness German Whispers Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 9, 0, 5, 0],
        [0, 2, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 8), (4, 7), (3, 6), (3, 5), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (6, 7), (6, 6), (5, 7)])
    puzzle.add_german_whispers([(7, 3), (6, 4), (7, 5), (7, 4), (8, 4)])
    puzzle.add_german_whispers([(1, 1), (2, 2), (3, 2), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(1, 5), (1, 6), (2, 7), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 1), (5, 2), (4, 2), (4, 1)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (7, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 2), (2, 3), (2, 4)])
    puzzle.add_german_whispers([(6, 2), (5, 3), (4, 3)])

    return puzzle
