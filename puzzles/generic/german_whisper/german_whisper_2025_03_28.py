"""PuzzleMadness German Whispers Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (4, 1), (4, 2), (5, 2), (5, 3), (4, 3)])
    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 3), (6, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (8, 7), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (2, 7), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(1, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (1, 2), (0, 1)])
    puzzle.add_german_whispers([(8, 3), (8, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(2, 3), (2, 4), (3, 5)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (7, 0)])

    return puzzle
