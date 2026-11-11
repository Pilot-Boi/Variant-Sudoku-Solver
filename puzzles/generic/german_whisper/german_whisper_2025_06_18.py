"""PuzzleMadness German Whispers Sudoku — 2025-06-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 3, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 7, 0, 0, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 0), (3, 1), (2, 1), (3, 2), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (2, 3), (2, 4), (3, 5)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (7, 4), (7, 5), (8, 5)])
    puzzle.add_german_whispers([(2, 5), (1, 6), (0, 7), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(6, 5), (7, 6), (6, 7), (5, 7)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (5, 3), (5, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(0, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (4, 8)])

    return puzzle
