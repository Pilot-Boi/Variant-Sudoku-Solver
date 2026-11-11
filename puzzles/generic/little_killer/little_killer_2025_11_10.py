"""PuzzleMadness Little Killer Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 1, 2, 8, 0, 0, 0],
        [0, 0, 2, 3, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 6, 0],
        [0, 0, 0, 0, 8, 4, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 34, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 19, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 48, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 39, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 24, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 28, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 30, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 6, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 36, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 31, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 25, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 35, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 50, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 12, clue_position=(1, 3, 3))

    return puzzle
