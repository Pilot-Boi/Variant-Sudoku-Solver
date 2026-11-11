"""PuzzleMadness German Whispers Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 2, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 3), (0, 4), (1, 4), (2, 5), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(8, 1), (7, 0), (7, 1), (8, 2), (7, 2)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (6, 4), (5, 4), (5, 3)])
    puzzle.add_german_whispers([(8, 6), (7, 5), (7, 6), (8, 7), (7, 8)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (3, 4), (3, 3)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 7), (0, 6)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(5, 8), (6, 7), (5, 7), (4, 8)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (1, 1)])
    puzzle.add_german_whispers([(3, 1), (2, 2), (2, 1)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (3, 7)])

    return puzzle
