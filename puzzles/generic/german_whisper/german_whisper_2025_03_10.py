"""PuzzleMadness German Whispers Sudoku — 2025-03-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 2), (1, 1), (0, 2), (1, 3), (1, 4), (2, 3)])
    puzzle.add_german_whispers([(2, 7), (3, 6), (4, 6), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (6, 2), (5, 2), (5, 3)])
    puzzle.add_german_whispers([(7, 3), (8, 2), (7, 1), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (6, 8), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(6, 6), (6, 5), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(3, 1), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(1, 8), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (3, 4)])

    return puzzle
