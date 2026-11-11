"""PuzzleMadness German Whispers Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 2), (5, 3), (4, 2), (3, 2), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(3, 6), (4, 6), (5, 7), (4, 7), (5, 8)])
    puzzle.add_german_whispers([(2, 1), (2, 2), (3, 3), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(0, 7), (1, 6), (1, 5), (2, 5), (2, 4)])
    puzzle.add_german_whispers([(7, 5), (8, 5), (8, 6), (7, 7)])
    puzzle.add_german_whispers([(0, 4), (1, 3), (1, 4), (2, 3)])
    puzzle.add_german_whispers([(4, 0), (5, 0), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 3), (8, 4)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(1, 0), (0, 1), (0, 2)])

    return puzzle
