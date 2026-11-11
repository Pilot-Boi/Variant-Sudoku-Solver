"""PuzzleMadness Little Killer Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 1, 5, 0, 7, 0, 8, 0],
        [0, 2, 0, 0, 0, 0, 1, 6, 5],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 40, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 13, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 41, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 12, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 29, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 28, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 24, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 6, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 39, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 31, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 11, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 20, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 29, clue_position=(0, 4, 0))

    return puzzle
