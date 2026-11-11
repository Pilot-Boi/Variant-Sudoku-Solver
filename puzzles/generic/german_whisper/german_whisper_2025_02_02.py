"""PuzzleMadness German Whispers Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 6, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 7), (1, 6), (1, 5), (0, 6), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(4, 2), (3, 2), (4, 1), (3, 0), (3, 1)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (7, 1), (8, 2), (7, 2)])
    puzzle.add_german_whispers([(3, 7), (4, 7), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 4), (8, 3)])
    puzzle.add_german_whispers([(7, 6), (7, 5), (8, 5), (8, 6)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (6, 7), (6, 6)])
    puzzle.add_german_whispers([(2, 2), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (4, 3)])
    puzzle.add_german_whispers([(1, 7), (2, 6), (2, 7)])
    puzzle.add_german_whispers([(1, 3), (1, 4), (2, 4)])

    return puzzle
