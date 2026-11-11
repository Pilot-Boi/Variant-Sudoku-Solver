"""PuzzleMadness German Whispers Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 6), (3, 5), (2, 5), (1, 6), (1, 7), (0, 6)])
    puzzle.add_german_whispers([(7, 7), (6, 6), (5, 5), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(2, 4), (2, 3), (1, 2), (0, 2), (1, 3)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (5, 1), (6, 2), (7, 3)])
    puzzle.add_german_whispers([(3, 2), (3, 3), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(6, 1), (7, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(6, 3), (7, 4), (8, 4), (8, 3)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(1, 0), (2, 0), (3, 1)])

    return puzzle
