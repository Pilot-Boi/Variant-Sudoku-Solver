"""PuzzleMadness Little Killer Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
        [4, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 3, 0, 0, 1, 2, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 1, 0],
        [6, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 20, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 17, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 43, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 46, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 17, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 20, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 19, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 7), (1, 8)], 10, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 35, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 15, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 43, clue_position=(0, 1, 3))

    return puzzle
