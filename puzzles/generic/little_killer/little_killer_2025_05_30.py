"""PuzzleMadness Little Killer Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 8, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 2, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 3],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 0],
        [1, 0, 8, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 39, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 23, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 8, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 12, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 16, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 22, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 20, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 19, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 16, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 39, clue_position=(1, 6, 3))

    return puzzle
