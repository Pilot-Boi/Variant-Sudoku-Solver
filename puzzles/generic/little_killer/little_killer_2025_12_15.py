"""PuzzleMadness Little Killer Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 4, 6, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [2, 0, 1, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 7, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 4, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 6, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 24, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 32, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 23, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 23, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 10, clue_position=(1, 2, 0))

    return puzzle
