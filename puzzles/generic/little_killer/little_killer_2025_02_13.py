"""PuzzleMadness Little Killer Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 7, 1, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 4, 0],
        [0, 0, 0, 0, 0, 9, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 2, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 32, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 38, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 14, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 26, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 25, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 24, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 27, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 38, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 22, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 9, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 10, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 47, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 51, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 19, clue_position=(1, 5, 1))

    return puzzle
