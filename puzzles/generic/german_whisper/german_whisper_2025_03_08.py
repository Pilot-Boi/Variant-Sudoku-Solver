"""PuzzleMadness German Whispers Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 1, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 3), (6, 4), (7, 4), (6, 5), (5, 6), (4, 6)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (4, 8), (5, 7), (6, 6)])
    puzzle.add_german_whispers([(2, 5), (1, 4), (1, 3), (1, 2), (0, 1)])
    puzzle.add_german_whispers([(6, 7), (7, 6), (8, 7), (7, 8), (6, 8)])
    puzzle.add_german_whispers([(5, 4), (4, 3), (4, 2), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(3, 0), (2, 1), (2, 2), (3, 2)])
    puzzle.add_german_whispers([(1, 7), (2, 7), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(0, 5), (0, 6), (1, 5)])
    puzzle.add_german_whispers([(5, 3), (6, 3), (6, 2)])

    return puzzle
