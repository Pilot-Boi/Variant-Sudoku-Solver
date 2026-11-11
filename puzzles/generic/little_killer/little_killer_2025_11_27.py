"""PuzzleMadness Little Killer Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 5],
        [0, 0, 8, 9, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 1, 0, 0],
        [0, 3, 0, 0, 0, 8, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 0), (0, 1)], 10, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 39, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 10, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 35, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 33, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 30, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 24, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 15, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 41, clue_position=(0, 0, 0))

    return puzzle
