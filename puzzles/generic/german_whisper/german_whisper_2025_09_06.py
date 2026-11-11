"""PuzzleMadness German Whispers Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 2), (7, 1), (8, 2), (7, 3), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (1, 6), (2, 6), (3, 5)])
    puzzle.add_german_whispers([(2, 3), (3, 2), (2, 2), (1, 1), (2, 0)])
    puzzle.add_german_whispers([(6, 4), (7, 4), (6, 5), (5, 5), (5, 6)])
    puzzle.add_german_whispers([(5, 7), (4, 6), (4, 7), (3, 7), (3, 6)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (0, 8), (1, 7)])
    puzzle.add_german_whispers([(4, 3), (3, 4), (4, 4), (4, 5)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(4, 2), (5, 1), (6, 1)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (7, 6)])

    return puzzle
