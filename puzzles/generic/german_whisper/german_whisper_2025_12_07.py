"""PuzzleMadness German Whispers Sudoku — 2025-12-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 6, 7, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (2, 2), (3, 3), (3, 4), (2, 4), (1, 3)])
    puzzle.add_german_whispers([(5, 6), (6, 6), (6, 7), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (0, 1), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(3, 5), (4, 5), (5, 4), (6, 3), (7, 2)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (1, 7), (2, 8), (2, 7)])
    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (1, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (8, 6)])

    return puzzle
