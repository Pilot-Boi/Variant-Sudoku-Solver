"""PuzzleMadness German Whispers Sudoku — 2025-12-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 7), (5, 6), (6, 5), (7, 4), (8, 3), (7, 2)])
    puzzle.add_german_whispers([(3, 3), (4, 4), (3, 5), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 8), (7, 7), (8, 7), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(2, 6), (1, 5), (0, 5), (0, 6), (1, 7)])
    puzzle.add_german_whispers([(4, 2), (5, 1), (5, 0), (6, 1), (7, 1)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (2, 1), (1, 1)])
    puzzle.add_german_whispers([(4, 6), (4, 7), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(5, 3), (6, 2), (6, 3), (5, 4)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(1, 3), (2, 3), (2, 2)])

    return puzzle
