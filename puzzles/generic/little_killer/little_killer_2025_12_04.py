"""PuzzleMadness Little Killer Sudoku — 2025-12-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 6],
        [0, 2, 0, 5, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 3, 7, 0, 5],
        [0, 0, 0, 6, 0, 1, 0, 7, 3],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 14, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 26, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 34, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 30, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 51, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 43, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 34, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 53, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 39, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 25, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 23, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 32, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 25, clue_position=(0, 3, 3))

    return puzzle
