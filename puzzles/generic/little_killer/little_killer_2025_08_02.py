"""PuzzleMadness Little Killer Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 2, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [2, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 9, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 9, 4, 0, 0, 0, 0, 5],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 29, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 42, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 10, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 31, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 24, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 8, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 27, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 12, clue_position=(1, 2, 1))

    return puzzle
