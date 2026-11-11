"""PuzzleMadness German Whispers Sudoku — 2025-12-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 5), (6, 6), (7, 7), (6, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (0, 7), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(3, 5), (2, 4), (3, 3), (3, 4), (4, 5)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (5, 1), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(3, 0), (2, 0), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(5, 6), (5, 7), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(4, 4), (4, 3), (3, 2), (2, 1)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (2, 7)])

    return puzzle
