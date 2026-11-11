"""PuzzleMadness Little Killer Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 7, 0, 0, 0, 0, 0, 0],
        [9, 0, 6, 0, 0, 8, 0, 0, 0],
        [2, 1, 8, 0, 0, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 4, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 27, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 24, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 31, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 37, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 18, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 29, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 41, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 27, clue_position=(1, 5, 2))

    return puzzle
