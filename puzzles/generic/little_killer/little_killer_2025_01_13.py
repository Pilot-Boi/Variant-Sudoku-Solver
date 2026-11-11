"""PuzzleMadness Little Killer Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 8],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 5, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 45, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 52, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 52, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 22, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 7, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 10, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 32, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 30, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 25, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 19, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 8, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 37, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 18, clue_position=(0, 4, 3))

    return puzzle
