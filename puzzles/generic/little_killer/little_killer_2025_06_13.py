"""PuzzleMadness Little Killer Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 0, 2, 0, 0, 7],
        [0, 7, 4, 3, 1, 0, 0, 6, 9],
        [9, 0, 2, 0, 0, 0, 8, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 11, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 43, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 27, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 34, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 14, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 40, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 19, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 49, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 17, clue_position=(0, 6, 2))

    return puzzle
