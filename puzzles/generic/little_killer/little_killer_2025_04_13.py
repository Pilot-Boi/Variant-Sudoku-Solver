"""PuzzleMadness Little Killer Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 2, 0, 3, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 4, 0, 0],
        [1, 0, 0, 0, 7, 8, 0, 3, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 30, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 26, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 56, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 48, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 20, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 33, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 29, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 15, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 36, clue_position=(1, 9, 2))

    return puzzle
