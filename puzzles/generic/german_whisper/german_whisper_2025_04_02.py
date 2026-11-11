"""PuzzleMadness German Whispers Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 6), (4, 5), (4, 4), (4, 3), (3, 3), (3, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 5), (8, 6), (7, 6), (8, 7)])
    puzzle.add_german_whispers([(2, 7), (3, 8), (3, 7), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(0, 3), (0, 4), (1, 5), (1, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 7), (5, 8), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(7, 4), (6, 3), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(3, 1), (2, 0), (2, 1), (1, 1)])
    puzzle.add_german_whispers([(4, 1), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 3)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 0)])

    return puzzle
