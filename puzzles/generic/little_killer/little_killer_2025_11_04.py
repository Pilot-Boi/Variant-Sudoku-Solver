"""PuzzleMadness Little Killer Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 1, 0, 0, 0],
        [0, 6, 0, 0, 0, 3, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 4, 0, 0, 5, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 6, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 26, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 20, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 10, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 25, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 39, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 39, clue_position=(1, 9, 2))

    return puzzle
