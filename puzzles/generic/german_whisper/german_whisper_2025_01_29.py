"""PuzzleMadness German Whispers Sudoku — 2025-01-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [7, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 6, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 3), (5, 4), (5, 5), (4, 5), (5, 6), (4, 6)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (7, 5), (7, 4), (7, 3)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (4, 0), (3, 1), (3, 0)])
    puzzle.add_german_whispers([(0, 4), (1, 5), (2, 6), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (7, 7), (6, 6)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_german_whispers([(4, 4), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(2, 4), (1, 3), (0, 2)])
    puzzle.add_german_whispers([(7, 6), (6, 5), (6, 4)])

    return puzzle
