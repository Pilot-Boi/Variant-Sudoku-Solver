"""PuzzleMadness German Whispers Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 1), (2, 2), (2, 1), (1, 2), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (4, 7), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (8, 5), (7, 5), (8, 4)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 4), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 6), (2, 7)])
    puzzle.add_german_whispers([(3, 4), (2, 5), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(7, 1), (6, 2), (5, 1), (4, 2)])
    puzzle.add_german_whispers([(4, 5), (3, 5), (4, 4)])
    puzzle.add_german_whispers([(2, 3), (1, 4), (1, 3)])
    puzzle.add_german_whispers([(4, 1), (4, 0), (3, 0)])

    return puzzle
