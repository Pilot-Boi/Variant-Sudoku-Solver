"""PuzzleMadness Little Killer Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 6],
        [0, 8, 0, 0, 9, 0, 5, 0, 3],
        [7, 0, 5, 0, 0, 0, 0, 0, 0],
        [2, 6, 0, 5, 0, 0, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 0, 4, 8],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 19, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 49, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 29, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 44, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 20, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 20, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 30, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 24, clue_position=(1, 5, 0))

    return puzzle
