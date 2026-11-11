"""PuzzleMadness German Whispers Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [6, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 3, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 7), (1, 7), (0, 6), (1, 6), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(2, 1), (1, 2), (1, 3), (2, 2), (3, 2)])
    puzzle.add_german_whispers([(2, 3), (3, 3), (4, 4), (5, 3), (6, 4)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (4, 8), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (7, 6), (8, 5)])
    puzzle.add_german_whispers([(4, 2), (5, 1), (6, 1), (7, 2)])
    puzzle.add_german_whispers([(7, 5), (7, 4), (6, 3)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (0, 0)])

    return puzzle
