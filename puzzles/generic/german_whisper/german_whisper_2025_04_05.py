"""PuzzleMadness German Whispers Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 7), (5, 8), (4, 7), (3, 6), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (0, 2), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(2, 8), (3, 8), (2, 7), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(3, 1), (4, 1), (5, 1), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 4), (6, 5), (7, 5)])
    puzzle.add_german_whispers([(5, 6), (4, 5), (3, 5), (2, 4)])
    puzzle.add_german_whispers([(5, 5), (4, 4), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(6, 6), (7, 6), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(6, 3), (5, 2), (4, 2)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (1, 6)])

    return puzzle
