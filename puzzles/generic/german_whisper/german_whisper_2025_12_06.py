"""PuzzleMadness German Whispers Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 7, 0, 1],
        [0, 0, 0, 4, 0, 0, 0, 0, 3],
        [0, 0, 0, 5, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 4), (7, 4), (7, 5), (6, 6), (5, 6), (4, 5)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (4, 6), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (1, 4), (0, 3), (0, 2)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (2, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (7, 0), (6, 0)])

    return puzzle
