"""PuzzleMadness German Whispers Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 7), (0, 6), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(6, 0), (7, 1), (8, 0), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (4, 3), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(8, 5), (7, 6), (6, 6), (6, 7), (7, 7)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (3, 6), (4, 5)])
    puzzle.add_german_whispers([(7, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 0)])
    puzzle.add_german_whispers([(1, 0), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(4, 6), (3, 7), (2, 7)])

    return puzzle
