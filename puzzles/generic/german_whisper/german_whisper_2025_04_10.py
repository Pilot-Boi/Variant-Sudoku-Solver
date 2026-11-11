"""PuzzleMadness German Whispers Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 3, 7, 0, 0, 0, 4],
        [0, 0, 2, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (0, 6), (1, 6), (1, 5), (2, 4), (1, 4)])
    puzzle.add_german_whispers([(6, 8), (5, 7), (4, 7), (5, 6), (4, 6)])
    puzzle.add_german_whispers([(7, 0), (6, 1), (6, 0), (5, 0), (4, 1)])
    puzzle.add_german_whispers([(4, 2), (3, 2), (3, 3), (3, 4), (4, 5)])
    puzzle.add_german_whispers([(2, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (7, 2), (8, 1)])
    puzzle.add_german_whispers([(6, 6), (7, 5), (6, 5)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (8, 8)])

    return puzzle
