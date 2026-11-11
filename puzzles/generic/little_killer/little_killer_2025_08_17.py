"""PuzzleMadness Little Killer Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 5, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 9],
        [0, 0, 7, 0, 0, 2, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 0, 3, 0, 8, 2, 0],
        [0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 5, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 14, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 25, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 41, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 40, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 34, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 34, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 25, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 42, clue_position=(0, -1, 0))

    return puzzle
