"""PuzzleMadness German Whispers Sudoku — 2025-09-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 9, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 7), (3, 6), (2, 5), (1, 5), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(3, 1), (2, 2), (2, 1), (1, 2), (0, 3)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (6, 2), (6, 1), (5, 1)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (5, 3), (5, 2), (4, 1)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (8, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (6, 0), (5, 0)])
    puzzle.add_german_whispers([(8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_german_whispers([(5, 6), (5, 5), (4, 6), (4, 5)])
    puzzle.add_german_whispers([(0, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 8)])
    puzzle.add_german_whispers([(2, 3), (3, 3), (4, 2)])

    return puzzle
