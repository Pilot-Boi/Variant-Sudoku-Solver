"""PuzzleMadness German Whispers Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 4), (6, 3), (5, 4), (5, 5)])
    puzzle.add_german_whispers([(3, 8), (2, 7), (2, 6), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(8, 7), (7, 7), (6, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(1, 5), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (5, 1), (4, 2)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (1, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 0), (4, 1), (3, 1), (2, 2)])
    puzzle.add_german_whispers([(4, 4), (4, 3), (5, 2)])
    puzzle.add_german_whispers([(8, 5), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (5, 6)])
    puzzle.add_german_whispers([(0, 3), (1, 4), (2, 3)])

    return puzzle
